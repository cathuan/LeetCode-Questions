import numpy as np


class Solution(object):
    def findMaxAverage(self, nums, k):
        minBound, maxBound = min(nums), max(nums)
        nums = np.array([0] + nums)

        while maxBound - minBound > 1e-5:
            mid = (minBound + maxBound) / 2.
            if self.isGreater(mid, nums, k):
                minBound = mid
            else:
                maxBound = mid
        return minBound

    def isGreater(self, mid, nums, k):
        nums[0] = mid
        sums = (nums - mid).cumsum()
        mins = np.minimum.accumulate(sums)
        return (sums[k:] - mins[:-k]).max() > 0


if __name__ == "__main__":
    nums = [8, 9, 3, 1, 8, 3, 0, 6, 9, 2]
    k = 8
    print Solution().findMaxAverage(nums, k)
