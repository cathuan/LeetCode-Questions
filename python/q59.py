class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = self.constructZeroMatrix(n)
        value = 1
        for index in range((n+1)/2):
            value = self.generateMatrixByStart(index, index, n-2*index, value, matrix)
        return matrix

    def generateMatrixByStart(self, i, j, length, start_value, matrix):

        if length == 1:
            matrix[i][j] = start_value
            return start_value + 1

        step = 1
        value = start_value
        while step < length:
            #print i, j, value
            matrix[i][j] = value
            value += 1
            step += 1
            j += 1

        step = 1
        while step < length:
            #print i, j, value
            matrix[i][j] = value
            value += 1
            step += 1
            i += 1

        step = 1
        while step < length:
            #print i, j, value
            matrix[i][j] = value
            value += 1
            step += 1
            j -= 1

        step = 1
        while step < length:
            #print i, j, value
            matrix[i][j] = value
            value += 1
            step += 1
            i -= 1

        return value

    def constructZeroMatrix(self, n):

        matrix = []
        for i in range(n):
            line = []
            for i in range(n):
                line.append(0)
            matrix.append(line)
        return matrix


def pprint(matrix):

    for line in matrix:
        print " ".join(str(i) for i in line)

if __name__ == "__main__":

    #matrix = generateMatrix(10)
    matrix = Solution().generateMatrix(5)
    pprint(matrix)
