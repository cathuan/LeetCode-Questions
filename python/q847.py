from collections import deque


class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        # store (currentNode, length, visitedBitMap) in queue
        queue = deque((i, 0, (1 << i)) for i in range(len(graph)))
        complete = 0
        for i in range(len(graph)):
            complete = complete | (1 << i)

        # if we have achieved the same or better situation before, we won't push the
        # new state into the queue.
        visitedDict = {}
        for node, count, visited in queue:
            visitedDict[(node, count)] = visited

        while queue:
            node, count, visited = queue.popleft()
            for nextNode in graph[node]:
                nextCount = count + 1
                nextVisited = visited | (1 << nextNode)
                if (nextNode, nextVisited) not in visitedDict:
                    visitedDict[(nextNode, nextVisited)] = nextCount
                    queue.append((nextNode, nextCount, nextVisited))
                elif nextCount < visitedDict[(nextNode, nextVisited)]:
                    visitedDict[(nextNode, nextVisited)] = nextCount
                    queue.append((nextNode, nextCount, nextVisited))
                if nextVisited == complete:
                    return nextCount
        return 0


if __name__ == "__main__":

    graph = [[2, 3, 5, 7], [2, 3, 7], [0, 1], [0, 1], [7],
             [0], [10], [9, 10, 0, 1, 4], [9], [7, 8], [7, 6]]
    print Solution().shortestPathLength(graph)
