import numpy as np


class Solution(object):

    @profile
    def minPathSum(self, grid):
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

        matrix = []
        for i in range(nRows):
            row = []
            for j in range(nCols):
                row.append(-1)
            matrix.append(row)

        matrix[nRows-1][nCols-1] = grid[nRows-1][nCols-1]

        for i in range(nRows-1, -1, -1):
            for j in range(nCols-1, -1, -1):
                if i == nRows-1 and j == nCols - 1:
                    matrix[i][j] = grid[i][j]
                    continue
                right_value = self.test_right(i, j, nRows, nCols, grid, matrix)
                down_value = self.test_down(i, j, nRows, nCols, grid, matrix)
                matrix[i][j] = min(right_value, down_value)

        return matrix[0][0]

    def test_down(self, i, j, nRows, nCols, grid, matrix):

        if i == nRows - 1:
            return np.inf
        else:
            return grid[i][j] + matrix[i+1][j]

    def test_right(self, i, j, nRows, nCols, grid, matrix):

        if j == nCols - 1:
            return np.inf
        else:
            return grid[i][j] + matrix[i][j+1]


if __name__ == "__main__":

    grid = [[1]*100]*100
    print Solution().minPathSum(grid)
