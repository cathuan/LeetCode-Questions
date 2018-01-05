import sys


class Solution(object):

    def div_by_multiplier(self, num, divisor):

        n = 1
        print "**", num, divisor
        while num % (divisor ** n) == 0:
            n *= 2

        return num / (divisor ** (n/2)), n/2

    def div(self, num, dividor):

        num, n = self.div_by_multiplier(num, dividor)
        while n != 0:
            print num, n
            num, n = self.div_by_multiplier(num, dividor)

        return num

    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """

        if num == 0:
            return False

        factors = [2,3,5]

        for factor in factors:
            num = self.div(num, factor)

        return num == 1


if __name__ == "__main__":

    num = int(sys.argv[1])
    solution = Solution()
    print solution.isUgly(num)
