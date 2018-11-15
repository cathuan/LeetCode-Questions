class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 1

        i = 0
        while i < len(nums):
            value = nums[i]
            if value > 0 and value <= len(nums) and nums[i] != i+1 and nums[value-1] != value:
                tmp = nums[value-1]
                nums[value-1] = value
                nums[i] = tmp
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1


if __name__ == "__main__":

    nums = [1,1]
    print Solution().firstMissingPositive(nums)