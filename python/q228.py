class Solution(object):

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        if len(nums) == 0:
            return []

        current_start = nums[0]
        summary = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            else:
                summary.append(self.getStr(current_start, nums[i-1]))
                current_start = nums[i]

        summary.append(self.getStr(current_start, nums[-1]))

        return summary

    def getStr(self, start, end):

        if start == end:
            return str(start)
        else:
            return "%s->%s" % (start, end)


if __name__ == "__main__":

    nums = [-1,0,1,2,4,5,7]
    print Solution().summaryRanges(nums)
