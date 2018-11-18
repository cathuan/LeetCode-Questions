from collections import defaultdict


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):

        graph = self.constructGraph(edges)

        # number of nodes in the subtree rooted at node i
        count = [1] * N
        ans = [0] * N

        self.dfs(graph, count, ans, node=0, parent=None)
        self.dfs2(N, graph, count, ans, node=0, parent=None)
        return ans

    def constructGraph(self, edges):
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        return graph

    # the first step of dfs. Modify ans and count such that
    # count[i] = number of nodes in subtree rooted with node i
    # ans[i] = path sum of node i to all nodes in the subtree rooted with node i
    def dfs(self, graph, count, ans, node, parent):
        for child in graph[node]:
            if child != parent:
                self.dfs(graph, count, ans, child, node)
                count[node] += count[child]
                ans[node] += ans[child] + count[child]

    # from top to bottom, makes ans[i] = path sum to all nodes.
    # idea is if j is the child of i, and ans[i] has been modified. Then
    # ans[j] = ans[i] - count_of_nodes_in_subtree_of_j + count_of_rest_of_nodes
    def dfs2(self, N, graph, count, ans, node, parent):
        for child in graph[node]:
            if child != parent:
                ans[child] = ans[node] - count[child] + N - count[child]
                self.dfs2(N, graph, count, ans, child, node)