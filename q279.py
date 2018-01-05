import numpy as np
import sys


class Solution(object):

    def getPerfectSquareNums(self, n):
        perfect_square_nums = []
        max_sqrt = int(np.sqrt(n))
        for i in range(1, max_sqrt+1):
            perfect_square_nums.append(i**2)
        return perfect_square_nums

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """


if __name__ == "__main__":

    n = int(sys.argv[1])
    solution = Solution()
    print solution.numSquares(n)
