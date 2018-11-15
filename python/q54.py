class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        result = []
        nRows = len(matrix)
        if nRows == 0:
            return matrix
        nCols = len(matrix[0])
        if nCols == 0:
            return matrix

        index = 0
        rows = nRows - 2*index
        cols = nCols - 2*index
        while rows > 0 and cols > 0:
            self.generateMatrixByStart(index, index, rows, cols, matrix, result)
            index += 1
            rows = nRows - 2*index
            cols = nCols - 2*index
        return result

    def generateMatrixByStart(self, i, j, rows, cols, matrix, result):

        if rows == 1 and cols == 1:
            result.append(matrix[i][j])
            return
        elif rows == 1 and cols != 1:
            step = 1
            while step < cols:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                j += 1
            result.append(matrix[i][j])
            return
        elif rows != 1 and cols == 1:
            step = 1
            while step < rows:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                i += 1
            result.append(matrix[i][j])
            return
        elif rows != 1 and cols != 1:
            step = 1
            while step < cols:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                j += 1

            step = 1
            while step < rows:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                i += 1

            step = 1
            while step < cols:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                j -= 1

            step = 1
            while step < rows:
                #print i, j, value
                result.append(matrix[i][j])
                step += 1
                i -= 1

            return


def pprint(matrix):

    for line in matrix:
        print " ".join(str(i) for i in line)

if __name__ == "__main__":

    matrix = [
 [ 1, 2, 3, 10 ],
 [ 4, 5, 6, 11 ],
 [ 7, 8, 9, 12 ]
]
    result = Solution().spiralOrder(matrix)
    #pprint(matrix)
    print result
