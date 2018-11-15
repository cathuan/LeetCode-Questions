class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrixRowSum = []
        for row in matrix:
            curSum = 0
            rowSum = []
            for v in row:
                curSum += v
                rowSum.append(curSum)
            self.matrixRowSum.append(rowSum)
        self.matrix = matrix

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """

        rowSum = self.matrixRowSum[row]
        mod = val - self.matrix[row][col]
        for i in range(col, len(rowSum)):
            rowSum[i] += mod
        self.matrix[row][col] = val

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        ret = 0
        for row in range(row1, row2 + 1):
            if col1 == 0:
                rowSumLeft = 0
            else:
                rowSumLeft = self.matrixRowSum[row][col1 - 1]
            rowSumRight = self.matrixRowSum[row][col2]
            rowSum = rowSumRight - rowSumLeft
            ret += rowSum
        return ret


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)