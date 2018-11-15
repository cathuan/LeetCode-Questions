class Solution(object):

    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        cols = set()

        nRows = len(matrix)
        if nRows == 0:
            return matrix
        nCols = len(matrix[0])
        if nCols == 0:
            return matrix

        for i in range(nRows):
            for j in range(nCols):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(nRows):
            for j in range(nCols):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":

    matrix = [[0,1,0],[1,1,1]]
    Solution().setZeroes(matrix)
    print matrix
