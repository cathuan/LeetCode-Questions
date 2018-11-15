class Solution(object):
    
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        step = 0
        next_max_dis = nums[0]
        curr_max_dis = 0
        for i in range(1, len(nums)):
        	if i > curr_max_dis:
        		step += 1
        		curr_max_dis = next_max_dis
        	num = nums[i]
        	next_max_dis = min(max(i+num, next_max_dis), len(nums)-1)

        return step


if __name__ == '__main__':

	nums = [2,3,1,1,4]
	print Solution().jump(nums)


