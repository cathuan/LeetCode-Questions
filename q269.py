# Topological sort with dfs


class Solution(object):

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        ret = []
        graph = self.buildGraph(words)
        unmarked = set(graph.keys())
        tempMarked = set()
        permMarked = set()

        while len(unmarked) > 0:
            w = unmarked.pop()
            isDAG = self.dfs(w, graph, tempMarked, permMarked, ret)
            if not isDAG:
                return ""

        ret.reverse()
        return "".join(ret)

    def dfs(self, w, graph, tempMarked, permMarked, ret):
        if w in permMarked:
            return True
        if w in tempMarked:
            return False

        tempMarked.add(w)
        for child in graph[w]:
            isDAG = self.dfs(child, graph, tempMarked, permMarked, ret)
            if not isDAG:
                return False

        tempMarked.remove(w)
        permMarked.add(w)
        ret.append(w)
        return True

    def buildGraph(self, words):
        graph = {}

        # create vertices
        for word in words:
            for w in word:
                graph[w] = set()

        # connect vertices by edges
        for i in range(len(words)-1):
            word1, word2 = words[i], words[i+1]
            for w1, w2 in zip(word1, word2):
                if w1 == w2:
                    continue
                else:
                    graph[w1].add(w2)
                    break

        return graph


if __name__ == "__main__":

    print Solution().alienOrder(["a","b","ca","cc"])