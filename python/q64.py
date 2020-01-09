class Solution(object):

    def minPathSum(self, grid) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        nRows = len(grid)
        if nRows == 0:
            return 0
        nCols = len(grid[0])
        if nCols == 0:
            return 0

        for i in range(nRows-1, -1, -1):
            for j in range(nCols-1, -1, -1):
                if i < nRows - 1:
                    value = min(grid[i][j] + grid[i][j+1], grid[i][j] + grid[i+1][j]) if j < nCols - 1 \
                        else grid[i][j] + grid[i+1][j]
                else:
                    value = grid[i][j] + grid[i][j+1] if j < nCols - 1 else grid[i][j]
                
                grid[i][j] = value

        return grid[0][0]


if __name__ == "__main__":

    grid = [[1]*100]*100
    print(Solution().minPathSum(grid))
