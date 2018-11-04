from collections import deque, defaultdict


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # loop over all the edges and records all the parents.
        # in the meantime, record edges of the node with two parents.
        N = len(edges)  # N = number of edges = number of nodes, by assumption
        parents = [-1] * (N + 1)
        children = defaultdict(list)
        candidates = []
        for edge in edges:
            parent, child = edge
            if parents[child] == -1:
                parents[child] = parent
                children[parent].append(child)
            else:
                candidates.append([parents[child], child])
                candidates.append(edge)
                assert child not in children[parent]

        # if there are 2 candidates, remove the second one.
        if candidates:
            assert len(candidates) == 2
            node = edges[0][0]
            root = self.findRoot(parents, node)
            # it means that the resulting graph is a loop
            if root is None:
                return candidates[0]
            seenNodes = self.getGraphNodes(children, root)
            if len(seenNodes) == N:
                return candidates[1]
            else:
                return candidates[0]
        else:
            node = edges[0][0]
            nodeInCycle = self.findLoop(parents, node)
            edges.reverse()
            for edge in edges:
                parent, child = edge
                if child in nodeInCycle:
                    return edge

    # find the root of the graph based on the supplied node
    def findRoot(self, parents, node):
        seenNodes = set()
        while parents[node] != -1:
            if node in seenNodes:
                return None
            seenNodes.add(node)
            node = parents[node]
        return node

    # expand the graph and find all the connected nodes based on the given root
    def getGraphNodes(self, children, root):
        seenNodes = set()
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            seenNodes.add(node)
            for child in children[node]:
                queue.append(child)
        return seenNodes

    def findLoop(self, parents, node):
        seenNodes = []
        seenNodeSet = set()
        while node not in seenNodeSet:
            seenNodes.append(node)
            seenNodeSet.add(node)
            node = parents[node]

        index = seenNodes.index(node)
        return set(seenNodes[index:])


if __name__ == "__main__":

    print Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4],
                                                      [4, 1], [1, 5]])
    print Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]])
    print Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [1, 3],
                                                      [4, 1]])
    print Solution().findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2],
                                                      [1, 4]])
    print Solution().findRedundantDirectedConnection([[2, 1], [1, 2], [2, 3]])
