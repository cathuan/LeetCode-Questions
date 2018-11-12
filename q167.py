class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(numbers) <= 1:
            return None

        start, end = 0, len(numbers)-1
        while start < end:
            num1, num2 = numbers[start], numbers[end]
            if num1 + num2 < target:
                start += 1
            elif num1 + num2 > target:
                end -= 1
            else:
                return [start+1, end+1]
        return None
        