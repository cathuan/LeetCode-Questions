class Solution(object):

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_accessable_index = 0
        prev_max_accessable_index = -1
        current_max_accessable_index = 0

        while current_max_accessable_index != len(nums)-1 and prev_max_accessable_index != current_max_accessable_index:
            prev_max_accessable_index, current_max_accessable_index = self.isExtendable(nums, prev_max_accessable_index, current_max_accessable_index)

        if current_max_accessable_index == len(nums)-1:
            return True
        elif prev_max_accessable_index == current_max_accessable_index:
            return False
        else:
            assert False

    def isExtendable(self, nums, prev_max_accessable_index, current_max_accessable_index):

        max_position = -1
        for index in range(prev_max_accessable_index+1, current_max_accessable_index+1):
            current_max_position = index + nums[index]
            max_position = max(current_max_position, max_position)
        max_position = min(max_position, len(nums)-1)
        return current_max_accessable_index, max_position


if __name__ == "__main__":

    nums = range(25000,0,-1)
    print Solution().canJump(nums)
