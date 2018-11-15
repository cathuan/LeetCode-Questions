import sys


class Solution(object):

    def remove(self, nums, flags, index):

        num = nums[index]
        local_index = index + num
        while local_index < len(nums):
            flags[local_index] = False
            local_index += num

        new_index = index + 1
        while new_index < len(nums) and not flags[new_index]:
            new_index += 1
        return num, flags, new_index

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = range(2,n)
        flags = [True] * len(nums)
        index = 0

        while index < len(nums):
            prime, flags, index = self.remove(nums, flags, index)
            print prime


if __name__ == "__main__":

    n = int(sys.argv[1])
    solution = Solution()
    solution.countPrimes(n)
