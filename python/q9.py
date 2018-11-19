import numpy as np


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        if x == 0:
            return True

        length = int(np.log(x) / np.log(10)) + 1

        front = (x - x / (10**((length + 1) / 2))) / (10**((length + 1) / 2))
        end = x % (10**(length / 2))

        print front, end, length

        return (front + end) % 11 == 0


if __name__ == "__main__":

    solution = Solution()

    s = solution.isPalindrome(11)
    print s
