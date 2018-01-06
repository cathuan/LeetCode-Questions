import numpy as np
import sys


class PerfectSquares(object):

    def __init__(self):
        self.perfectSquares = [1]
        self.current_max = 1

    def request(self, n):
        if n < (self.current_max + 1) ** 2:
            return self.perfectSquares
        else:
            self.current_max += 1
            self.perfectSquares.append(self.current_max ** 2)
            return self.perfectSquares


# 62.15%. Not good, apparantly.
class Solution(object):

    @profile
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        perfect_squares_getter = PerfectSquares()
        solved = [0]

        for val in range(1,n+1):
            perfect_squares = perfect_squares_getter.request(val)
            solved.append(min(solved[-p] for p in perfect_squares)+1)

        return solved[n]


if __name__ == "__main__":

    n = int(sys.argv[1])
    print Solution().numSquares(n)
