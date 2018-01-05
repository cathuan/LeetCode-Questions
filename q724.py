class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        index = 0
        left_sum = 0
        right_sum = sum(nums[1:])
        while index < len(nums):
            if left_sum == right_sum:
                return index
            left_sum += nums[index]
            right_sum -= nums[index+1] if index < len(nums)-1 else 0
            index += 1

        return -1
