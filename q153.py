class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return -1

        return nums[self.findChangePoint(nums)]

    def findChangePoint(self, nums):

        i, j = 0, len(nums)-1

        # if the list is already sorted
        if nums[i] < nums[j]:
            return 0

        mid = (i + j) // 2
        while j - i > 1:
            if nums[mid] > nums[i]:
                i = mid
            else:
                j = mid
            mid = (i + j) // 2
        return j
