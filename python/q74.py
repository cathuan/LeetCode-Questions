class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        nRows = len(matrix)
        if nRows == 0:
            return False
        nCols = len(matrix[0])
        if nCols == 0:
            return False

        i = 0
        j = nRows * nCols - 1
        if self.getValue(i, matrix, nCols) > target:
            return False
        if self.getValue(j, matrix, nCols) < target:
            return False

        if i == j:
            return self.getValue(i, matrix, nCols) == target

        if self.getValue(i, matrix, nCols) == target:
            return True
        if self.getValue(j, matrix, nCols) == target:
            return True

        while j - i > 1:

            mid = (i+j)//2
            if self.getValue(mid, matrix, nCols) == target:
                return True
            elif self.getValue(mid, matrix, nCols) < target:
                i = mid
            else:
                j = mid
        return False


    def getValue(self, n, matrix, nCols):

        i = n // nCols
        j = n - i * nCols
        return matrix[i][j]


if __name__ == "__main__":

    matrix = [[1,3,5]]

    print Solution().searchMatrix(matrix, 1)
