class Solution(object):

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # special cases
        if len(matrix) == 0:
            return matrix

        if len(matrix[0]) == 0:
            return matrix

        nRows = len(matrix)
        nCols = len(matrix[0])

        # all position 1 squares:

        for i in range(nCols/2):
            for j in range((nRows+1)/2):
                i_1, j_1 = i, j
                i_2, j_2 = self.find_next_position(i_1, j_1, nRows, nCols)
                i_3, j_3 = self.find_next_position(i_2, j_2, nRows, nCols)
                i_4, j_4 = self.find_next_position(i_3, j_3, nRows, nCols)
                i_5, j_5 = self.find_next_position(i_4, j_4, nRows, nCols)
                assert i_1 == i_5 and j_1 == j_5

                val1 = matrix[i_1][j_1]
                val2 = matrix[i_2][j_2]
                val3 = matrix[i_3][j_3]
                val4 = matrix[i_4][j_4]

                print val1, val2, val3, val4
                new_v1, new_v2, new_v3, new_v4 = self.swap_four_elements(val1, val2, val3, val4)
                matrix[i_1][j_1] = new_v1
                matrix[i_2][j_2] = new_v2
                matrix[i_3][j_3] = new_v3
                matrix[i_4][j_4] = new_v4

    def swap_four_elements(self, a, b, c, d):

        return d, a, b, c

    def find_position(self, i, j, nRows, nCols):

        if i < nCols/2:
            if i <= nRows/2:
                return 1
            else:
                return 2
        else:
            if i < nRows/2:
                return 4
            else:
                return 3

    def find_next_position(self, i, j, nRows, nCols):

        position = self.find_position(i,j,nRows, nCols)
        connors = {1: (0,0), 2: (0,nCols-1), 3:(nRows-1,nCols-1), 4:(nRows-1,0)}

        old_connor_i, old_connor_j = connors[position]
        new_position = position + 1 if position != 4 else 1
        new_connor_i, new_connor_j = connors[new_position]

        old_i_distance = abs(i - old_connor_i)
        old_j_distance = abs(j - old_connor_j)

        if new_connor_i == 0:
            new_i = new_connor_i + old_j_distance
        else:
            new_i = new_connor_i - old_j_distance

        if new_connor_j == 0:
            new_j = new_connor_j + old_i_distance
        else:
            new_j = new_connor_j - old_i_distance

        return new_i, new_j


if __name__ == "__main__":

    matrix = \
        [
          [1,2,3],
          [4,5,6],
          [7,8,9]
        ]

    solution = Solution()
    solution.rotate(matrix)
    print matrix
    #print solution.find_next_position(0,1,4,4)
