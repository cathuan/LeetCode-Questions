
# 25.93%
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        length = 0
        sign = None
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                new_sign = 1
            elif nums[i] < nums[i-1]:
                new_sign = -1
            else:
                continue

            if sign is None:
                sign = new_sign
                length += 1
            elif new_sign != sign:
                sign = new_sign
                length += 1

        return length+1


if __name__ == "__main__":

    nums = [1,7,4,9,2,5]
    print Solution().wiggleMaxLength(nums)
