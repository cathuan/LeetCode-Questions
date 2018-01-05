import numpy as np


class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # make sure nums1 is shorter (or equal) to nums2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


    # find index i, such that nums[i] < n and nums[i+1] >= n (or i == len(nums)-1)
    def find_max_less_than(self, n, nums, i, j):

        print n, nums, i, j
        assert j > i
        v1 = nums[i]
        v2 = nums[j]

        # all less than n, then return j
        if v2 < n:
            return j

        # all greater than n, then return None, which means no solution
        if v1 >= n:
            return None

        # find adjacent indices, which bounds n. Then return i, the smaller one.
        if j - i == 1:
            return i

        k = (i + j)/2
        if nums[k] >= n:
            return self.find_max_less_than(n, nums, i, k)
        else:
            return self.find_max_less_than(n, nums, k, j)

    # find index i, such that nums[i] > n and nums[i-1] <= n (or i == 0)
    def find_min_greater_than(self, n, nums, i, j):

        print n, nums, i, j, "greater"
        assert j > i
        v1 = nums[i]
        v2 = nums[j]

        # all less than n, then return None, which means no solution
        if v2 <= n:
            return None

        # all greater than n, then return i
        if v1 > n:
            return i

        # find adjacent indices, which bounds n. Then return i, the smaller one.
        if j - i == 1:
            return j

        k = (i + j)/2
        if nums[k] > n:
            return self.find_min_greater_than(n, nums, i, k)
        else:
            return self.find_min_greater_than(n, nums, k, j)

    def test(self, nums1, nums2):

        return np.median(nums1 + nums2)


if __name__ == "__main__":

    nums = [1,2,3,4,4,5,5,5,6,6,7,8]
    solution = Solution()
