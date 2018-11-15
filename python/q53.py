import numpy as np

class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_value = 0
        current_value = 0
        current_max = -np.inf

        for num in nums:
            current_value += num
            current_max = max(current_max, current_value - min_value)
            min_value = min(min_value, current_value)

        return current_max


if __name__ == "__main__":

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(nums)
