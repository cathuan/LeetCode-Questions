class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        nrows = len(obstacleGrid)
        if nrows == 0:
            return 0
        ncols = len(obstacleGrid[0])

        dp = []
        for _ in range(nrows):
            dp.append([0] * ncols)

        for r in range(nrows - 1, -1, -1):
            for c in range(ncols - 1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                elif r == nrows - 1 and c == ncols - 1:
                    dp[r][c] = 1
                else:
                    if c == ncols - 1:
                        rightPath = 0
                    else:
                        rightPath = dp[r][c + 1]
                    if r == nrows - 1:
                        downPath = 0
                    else:
                        downPath = dp[r + 1][c]
                    dp[r][c] = rightPath + downPath

        return dp[0][0]


if __name__ == "__main__":

    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    print Solution().uniquePathsWithObstacles(grid)