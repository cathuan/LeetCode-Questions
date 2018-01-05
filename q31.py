class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        index = self.findReverseAscendingIndex(nums)

        if index == 0:
            self.reverse(nums, 0)
        else:
            self.findNext(nums, index-1)

    def findReverseAscendingIndex(self, nums):

        index = len(nums) - 1
        while index > 0:
            if nums[index] <= nums[index-1]:
                index -= 1
            else:
                break
        return index

    def reverse(self, nums, index):

        for i in range(index, (len(nums)+index)/2):
            nums[i], nums[len(nums)-1+index-i] = nums[len(nums)-1+index-i], nums[i]

    def findNext(self, nums, index):

        self.reverse(nums, index+1)
        print nums
        anchor = nums[index]
        for i in range(index+1, len(nums)):
            if nums[i] <= anchor:
                pass
            else:
                break
        nums[index], nums[i] = nums[i], nums[index]


if __name__ == "__main__":

    nums = [1,2,6,9,8,7,5,5,4,3,2]
    Solution().nextPermutation(nums, 2)
    print nums
