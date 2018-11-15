# The major problem is that, numbers can be duplicated. So sometimes, it's not easy to know that if
# mid == nums[h], whether the head is between mid and h or not. In such case, we let h =- 1.
# This makes the algorithm O(n) in worst case, but O(log(n)) in good cases.

# One example: [2,2,2,2,2,2,2,...,2,1,2,2,2,...,2]. In this case, if 1 is in a hard-to-find index, we
# have to use O(n).


class Solution(object):
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, h = 0, len(nums) - 1
        while l < h:
            mid = (h + l) / 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid if nums[h] != nums[mid] else h - 1
        return nums[l]