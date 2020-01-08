class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)
        nums = sorted(nums)
        result = float("inf")
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            second, third = i+1, n-1
            while second < third:
                sums = nums[i] + nums[second] + nums[third]
                if sums == target:
                    return target
                if abs(sums - target) < abs(result - target):
                    result = sums
                if sums < target:
                    second += 1
                else:
                    third -= 1
        return result