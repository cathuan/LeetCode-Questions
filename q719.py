from collections import deque


class SlidingWindow(object):

    def __init__(self, maxDif):
        self.data = deque()
        self.maxDif = maxDif

    def push(self, value):
        self.data.append(value)
        while value - self.data[0] > self.maxDif:
            self.data.popleft()

    def getLength(self):
        return len(self.data)


class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums = sorted(nums)
        lo, hi = 0, nums[-1] - nums[0]
        if self.countPairs(lo, nums) >= k:
            return lo
        if self.countPairs(hi-1, nums) < k:
            return hi

        while hi - lo > 1:
            mid = (lo + hi)/2
            # at most k-1 number of pairs with diff <= mid. Hence answer must > mid.
            if self.countPairs(mid, nums) < k:
                lo = mid
            # at least k number of pairs with diff <= mid. Hence answer must <= mid
            else:
                hi = mid
            mid = (hi + lo)/2

        if self.countPairs(lo, nums) < k:
            return hi
        else:
            return lo

    # return number of paris with difference <= maxDif

    def countPairs(self, maxDif, nums):

        count = 0
        window = SlidingWindow(maxDif)

        i = 0
        while i < len(nums) and nums[i] - nums[0] <= maxDif:
            window.push(nums[i])
            i += 1

        count += window.getLength() * (window.getLength()-1)/2
        for j in range(i, len(nums)):
            window.push(nums[j])
            count += window.getLength()-1
        return count


if __name__ == "__main__":

    print Solution().smallestDistancePair([1, 3, 1], 2)
