class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minStack = []
        minValue = float("inf")
        for num in nums:
            minValue = min(num, minValue)
            minStack.append(minValue)
        
        stack = []
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            minValue = minStack[i]
            if num == minValue:
                continue
            if not stack:
                stack.append(num)
                continue
            
            while stack and stack[-1] < minValue: