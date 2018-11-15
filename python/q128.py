class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        longest_seq = 0
        nums = set(nums)

        for num in nums:
        	if num - 1 in nums:
        		continue

        	current_num = num
        	current_seq_length = 1

        	while current_num + 1 in nums:
        		current_num += 1
        		current_seq_length += 1

        	longest_seq = max(longest_seq, current_seq_length)

        return longest_seq