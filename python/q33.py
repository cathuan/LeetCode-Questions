# 40ms, 28.8%
class Solution(object):


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        length = len(nums)
        if length == 0:
            return -1

        i = self.findChangePoint(nums)
        j = (i - 1) % length

        if nums[i] == target:
            return i
        if nums[j] == target:
            return j
        if target < nums[i] or target > nums[j]:
            return -1

        mid = ((i + j + length) // 2) % length if j < i else (i + j) // 2
        while (j - i) % length > 1:
            #assert nums[i] < nums[j]
            if nums[mid] < target:
                i = mid
            elif nums[mid] > target:
                j = mid
            else:
                return mid
            mid = ((i + j + length) // 2) % length if j < i else (i + j) // 2

        #assert nums[i] != target and nums[j] != target
        return -1

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
            #else:
            #    assert False
            mid = (i + j) // 2
        return j


if __name__ == "__main__":

    nums = [1000] + range(999)
    target = 2
    print Solution().search(nums, target)
