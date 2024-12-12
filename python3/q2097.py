from typing import List
from collections import defaultdict, deque


class Solution:
    def validArrangement(self, pairs):
        
        adjacencyMatrix = defaultdict(deque)
        inDegree, outDegree = defaultdict(int), defaultdict(int)

        # Build the adjacency list and track in-degrees and out-degrees
        for pair in pairs:
            start, end = pair
            adjacencyMatrix[start].append(end)
            outDegree[start] += 1
            inDegree[end] += 1

        result = []

        def visit(node):
            while adjacencyMatrix[node]:
                nextNode = adjacencyMatrix[node].popleft()
                visit(nextNode)
            result.append(node)

        # Find the start node (outDegree == 1 + inDegree )
        startNode = -1
        for node in outDegree:
            if outDegree[node] == inDegree[node] + 1:
                startNode = node
                break

        # If no such node exists, start from the first pair's first element
        if startNode == -1:
            startNode = pairs[0][0]

        # Start DFS traversal
        visit(startNode)

        # Reverse the result since DFS gives us the path in reverse
        result.reverse()

        # Construct the result pairs
        pairedResult = [[result[i - 1], result[i]] for i in range(1, len(result))]

        return pairedResult



if __name__ == "__main__":
    pairs = [[5,1],[4,5],[11,9],[9,4]]
    # pairs = [[1,3],[3,2],[2,1]]
    # pairs = [[1,2],[1,3],[2,1]]
    pairs = [[999,990],[356,511],[192,879],[246,945],[322,602],[776,246],[248,126],[503,284],[126,164],[494,731],[862,382],[731,578],[511,277],[122,731],[578,99],[731,277],[847,538],[246,494],[284,138],[382,899],[811,439],[164,99],[485,307],[618,320],[494,511],[413,248],[945,356],[990,614],[138,18],[164,862],[277,164],[826,737],[277,322],[618,122],[291,639],[288,11],[624,485],[740,452],[614,740],[307,903],[457,412],[538,961],[439,122],[961,999],[639,822],[903,503],[961,776],[138,538],[122,826],[99,138],[949,175],[452,847],[320,624],[879,457],[511,961],[835,692],[18,949],[737,413],[822,999],[11,726],[692,618],[899,835],[726,192],[999,452],[602,811],[452,618],[175,246],[99,291],[412,494]]
    print(Solution().validArrangement(pairs))