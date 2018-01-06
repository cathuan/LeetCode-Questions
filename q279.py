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
class Solution2(object):

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


"""
We can have a better solution if we have some number theory knowledge. The solution is O(sqrt(n)).

- By Lagrange's four-square theorem (https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem),
all numbers can be expressed as the sum of at most 4 square numbers.
- By Legendre's three-square theorem (https://en.wikipedia.org/wiki/Legendre's_three-square_theorem),
n = a^2 + b^2 + c^2 if and only if n = 4^k*(8l+7). We can test whether the output is 4 by this.
- Then we can using O(sqrt(n)) time to test whether n = a^2 or n = a^2 + b^2
- If not, output 3.
"""

# 93.52% feels good enough?
class Solution(object):

    @profile
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        while n % 4 == 0:
            n = n / 4
        if n % 8 == 7:
            return 4

        for i in xrange(int(np.floor(np.sqrt(n)))+1):
            if self.isSquare(n - i * i):
                if i == 0 or i * i == n:
                    return 1
                else:
                    return 2
        return 3

    def isSquare(self, n):
        return n == int(np.floor(np.sqrt(n))) ** 2


if __name__ == "__main__":

    n = int(sys.argv[1])
    print Solution().numSquares(n)
    #print Solution2().numSquares(n)
