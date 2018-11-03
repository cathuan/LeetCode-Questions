import bisect


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = [0]
        self.merge(nums, res)
        return res[0]

    def merge(self, nums, res):
        if len(nums) <= 1:
            return nums
        left, right = self.merge(nums[:len(nums)//2], res), self.merge(nums[len(nums)//2:], res)
        for r in right:
            add = len(left) - bisect.bisect(left, 2 * r)
            if not add:
                break
            res[0] += add
        return sorted(left+right)


if __name__ == "__main__":

    print Solution().reversePairs([2,4,3,5,1])