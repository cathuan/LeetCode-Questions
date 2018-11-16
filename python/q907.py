class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        stack = []
        ret = 0
        bufAns = 0

        for num in A:
            count = 1
            while stack and stack[-1][0] >= num:
                preNum, preCount = stack.pop()
                count += preCount
                bufAns -= preNum * preCount
            stack.append((num, count))
            bufAns += num * count
            ret += bufAns

        return ret % (10**9+7)
