class Solution(object):

	def maxSlidingWindow(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""

		if len(nums) == 0:
			return []

		splits = []
		current = []
		for num in nums:
			current.append(num)
			if len(current) == k:
				splits.append(current)
				current = []
		else:
			splits.append(current)
		
		leftMax = []
		for seqs in splits:
			current = []
			maxValue = float("-inf")
			for num in seqs:
				maxValue = max(maxValue, num)
				current.append(maxValue)
			leftMax.extend(current)

		rightMax = []
		for seqs in splits:
			current = []
			maxValue = float("-inf")
			for num in seqs[::-1]:
				maxValue = max(maxValue, num)
				current.append(maxValue)
			rightMax.extend(current[::-1])

		result = []
		for i in range(len(nums)-k+1):
			maxValue = max(leftMax[i+k-1], rightMax[i])
			result.append(maxValue)
		return result


if __name__ == '__main__':

	print Solution().maxSlidingWindow([1,3,1,2,4,2,3,6,4,3], 4)