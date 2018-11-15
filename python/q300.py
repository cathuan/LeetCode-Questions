import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        litSeq = []
        for num in nums:
            index = bisect.bisect_left(litSeq, num)
            if index == len(litSeq):
                litSeq.append(num)
            else:
                litSeq[index] = num
        return len(litSeq)