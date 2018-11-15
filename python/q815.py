from collections import defaultdict, deque


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        if S == T:
            return 0

        # transform route from list to set so it's easier to use
        # intersections to determine whether two routes are connected
        routes = [set(route) for route in routes]

        # cache connection between routes
        # j in connected[i] iff route i and route j have common stops
        connected = defaultdict(list)
        for i, route1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                route2 = routes[j]
                if route1.intersection(route2):
                    connected[i].append(j)
                    connected[j].append(i)

        # BFS
        # route has travelled. Used to ignore taking the same bus again.
        seen = set()  # record index of route
        queue = deque()
        for i, route in enumerate(routes):
            if S in route:
                queue.append((1, i))
                seen.add(i)

        while queue:
            routeCount, routeIndex = queue.popleft()
            route = routes[routeIndex]
            if T in route:
                return routeCount
            for j in connected[routeIndex]:
                if j not in seen:
                    queue.append((routeCount + 1, j))
                    seen.add(j)
        return -1