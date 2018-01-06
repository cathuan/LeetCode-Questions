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
        indices = [0, 0, 0]
        multiples = [2, 3, 5]

        while len(ugly_numbers) != n:
            new_generated_nums = [ugly_numbers[indices[i]]*multiples[i] for i in range(3)]
            min_value = min(new_generated_nums)
            for i in range(3):
                if min_value == new_generated_nums[i]:
                    indices[i] += 1
            ugly_numbers.append(min_value)

        return ugly_numbers[-1]


if __name__ == "__main__":

    n = 10
    print Solution().nthUglyNumber(n)
