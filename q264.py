"""
Manage three indices i2, i3 and i5, so that ugly_numbers[i2] is the first known ugly number such
ugly_numbers[i2]*2 > max known ugly number. Similar for i3 and i5.
Then, the smallest ugly_numbers[i2]*2, ugly_numbers[i3]*3 and ugly_numbers[i5]*5 is the next
ugly number. We increment the corresponding index.
Note sometimes there are more than one min numbers. We need to increment both indices.
"""


class Solution(object):

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        ugly_numbers = [1]
        i2, i3, i5 = 0, 0, 0

        while len(ugly_numbers) != n:
            v2, v3, v5 = ugly_numbers[i2]*2, ugly_numbers[i3]*3, ugly_numbers[i5]*5
            min_value = min(v2, v3, v5)

            if min_value == v2:
                i2 += 1
            if min_value == v3:
                i3 += 1
            if min_value == v5:
                i5 += 1

            ugly_numbers.append(min_value)

        return ugly_numbers[-1]


if __name__ == "__main__":

    n = 1000
    print Solution().nthUglyNumber(n)
