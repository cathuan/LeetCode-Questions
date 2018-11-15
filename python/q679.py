# Use Brute Force to solve this question, since there are only 4 cards, there are 9216 possibles.
# - choose 2 numbers randomly and use +,-,*,/ to do the cal  (12*4)
# - put the result back, and choose 2 numbers from the new nums and do ops (6*4)
# - put the result back, and choose 2 numbers from the new nums and do ops (2*4)
# - check output  (12*6*4*4*4=)
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-3

        # choose two numbers from nums
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                num1, num2 = nums[i], nums[j]
                rests = [nums[k] for k in range(len(nums)) if (k != i and k != j)]
                rests.append(num1 + num2)
                if self.judgePoint24(rests):
                    return True
                rests.pop()

                rests.append(num1 - num2)
                if self.judgePoint24(rests):
                    return True
                rests.pop()

                rests.append(num1 * num2)
                if self.judgePoint24(rests):
                    return True
                rests.pop()

                if num2 != 0:
                    rests.append(num1 * 1.0 / num2)
                    if self.judgePoint24(rests):
                        return True
        return False