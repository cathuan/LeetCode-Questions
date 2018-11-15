# a ^ b = the "or" computation for a and b by considering them as bits
# a & b = the "and" computation for a and b by considering them as bits

# Suppose a and b are two numbers we want to find
# 82.88%. Not too bad. 37ms for 30 tests.
class Solution(object):

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        xor = self.findBinarySumOfAllNumbers(nums)
        bit = self.findMinimalNonzeroBit(xor)
        return self.findNums(nums, bit)

    # because a ^ a = 0, the return of this function is a^b.
    def findBinarySumOfAllNumbers(self, nums):

        xor = 0
        for num in nums:
            xor = xor ^ num
        return xor

    # find bit with the lowest non zero
    # note that as a ^ b != 0, there must be a nonzero bit in a ^ b.
    # If this bit represents number x, then either a & x = 0, b & x != 0, or
    # a & x = 0, b & x != 0.
    def findMinimalNonzeroBit(self, xor):

        bit = 1
        while bit & xor == 0:
            bit = bit * 2  # move bit left by one
        return bit

    # suppose $bit is a nonzero bit. Then we can use it to separate nums into
    # two groups: S={x \in nums | x & bit = 0} and T={x \in nums | x & bit != 0}
    # Not that if a \in S, then b \not\in S and vice versa. Similar for T.
    # So the ^ sum of S = a, and ^ sum of T = b, because all the other numbers
    # appear in pairs.
    def findNums(self, nums, bit):

        a = 0
        b = 0
        for num in nums:
            if num & bit == 0:
                a = a ^ num
            else:
                b = b ^ num
        return a, b


if __name__ == "__main__":

    nums = [1,2,1,3,2,5]
    print(Solution().singleNumber(nums))
