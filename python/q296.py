class Solution(object):

    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # if the grid is empty
        if not len(grid):
            return None
        if not len(grid[0]):
            return None

        rows = self.getRows(grid)
        cols = self.getCols(grid)
        rowDist = self.getMinDist(rows)
        colDist = self.getMinDist(cols)
        return rowDist + colDist

    def getRows(self, grid):
        return [sum(row) for row in grid]

    def getCols(self, grid):
        cols = [0] * len(grid[0])
        for row in grid:
            cols = [c+v for c, v in zip(cols, row)]
        return cols

    def getMinDist(self, values):
        curMinDist = 0
        for i, v in enumerate(values):
            curMinDist += i*v
        minDist = curMinDist

        left = [0]*(len(values))
        for i in range(1, len(values)):
            left[i] = left[i-1] + values[i-1]
        right = [0]*(len(values))
        for i in range(1, len(values)):
            j = len(values)-1-i
            right[j] = right[j+1] + values[j+1]

        curPos = 1
        while curPos < len(values):
            curMinDist = curMinDist + left[curPos] - right[curPos-1]
            minDist = min(minDist, curMinDist)
            curPos += 1
        return minDist


if __name__ == "__main__":
    print Solution().minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])