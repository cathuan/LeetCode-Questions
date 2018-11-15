"""
For a number, it's kth (k starts by 0) binary digit is 1 if it's between
[2^k,2*2^k-1], [3*2^k,4*2^k-1],...,[(2l+1)*2^k, (2l+2)*2^k-1],...
so, if the AND of all numbers between m and n has kth binary digit to be 1 if and only if we can
find l such that there exists an odd number o:
o * 2^k <= m <= n < (o+1)*2^k, which is equivalent to
floor(m / 2^k) == floor(n / 2^k) == odd
"""

class Solution(object):

    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        divisor = 1
        result = 0
        diff = n - m
        while divisor <= diff:
            divisor *= 2

        while divisor <= n:
            m_quot = int(m/divisor)
            n_quot = int(n/divisor)

            if m_quot == n_quot and m_quot % 2 == 1:
                result += divisor

            divisor *= 2

        return result


if __name__ == "__main__":

    print Solution().rangeBitwiseAnd(72849572,72950122)
