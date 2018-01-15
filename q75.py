class Solution(object):

    def sortColors(self, nums):

        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]

        for num in nums:
            counts[num] += 1

        red = counts[0]
        blue = counts[0] + counts[1]

        for i in range(len(nums)):
            if i < red:
                nums[i] = 0
            elif i < blue:
                nums[i] = 1
            else:
                nums[i] = 2
                    
