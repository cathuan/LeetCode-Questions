import heapq


class Node(object):

    def __init__(self, row, col, height):
        self.row = row
        self.col = col
        self.height = height

    def __lt__(self, other):
        return self.height < other.height

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return "(%s, %s) %s" % (self.row, self.col, self.height)


class Solution(object):

    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        nRows = len(heightMap)
        if nRows == 0 or nRows == 1:
            return 0
        nCols = len(heightMap[0])
        if nCols == 0 or nCols == 1:
            return 0

        heap = []
        visitedNodes = set()

        for row in range(nRows):
            if row == 0 or row == nRows-1:
                for col in range(nCols):
                    node = Node(row, col, heightMap[row][col])
                    heapq.heappush(heap, node)
                    visitedNodes.add((node.row, node.col))
            else:
                for col in [0, len(heightMap[row])-1]:
                    node = Node(row, col, heightMap[row][col])
                    heapq.heappush(heap, node)
                    visitedNodes.add((node.row, node.col))

        maxHeight = 0
        water = 0

        while len(heap) > 0:
            node = heapq.heappop(heap)
            if node.height > maxHeight:
                maxHeight = node.height
            else:
                water += maxHeight - node.height
            
            for row, col in [(node.row-1, node.col), (node.row+1, node.col), 
                             (node.row, node.col-1), (node.row, node.col+1)]:
                if 0 <= row <= nRows-1 and 0 <= col <= nCols-1:
                    node = Node(row, col, heightMap[row][col])
                    if (row, col) not in visitedNodes:
                        heapq.heappush(heap, node)
                        visitedNodes.add((node.row, node.col))
    
        return water


if __name__ == "__main__":

    heightMap = [
        [1,4,3,1,3,2],
        [3,2,1,3,2,4],
        [2,3,3,2,3,1]
    ]
    print Solution().trapRainWater(heightMap)