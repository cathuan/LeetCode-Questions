class Solution(object):

    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        for i in range(0,n+1):
            count += self.count_with_digit(i)
        return count

    def count_with_digit(self, k):

        if k == 0:
            return 1

        k -= 1
        result = 9
        n = 9
        while k >= 1:
            result *= n
            n -= 1
            k -= 1
        return result
