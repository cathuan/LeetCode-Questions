class Solution(object):

	def maxNumber(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""

		result = []
		for n1 in range(max(k-len(nums2), 0), min(len(nums1)+1, k+1)):
			n2 = k - n1
			r1 = self.findMaxArray(nums1, n1)
			r2 = self.findMaxArray(nums2, n2)
			r = self.merge(r1,r2)
			result = max(result, r)
		return result

	def findMaxArray(self, nums, n):

		drop = len(nums) - n
		result = []
		for num in nums:
			while drop > 0 and (len(result) > 0 and result[-1] < num):
				result.pop()
				drop -= 1
			result.append(num)
		return result[:n]

	def merge(self, nums1, nums2):
		result = []
		while len(nums1) + len(nums2) > 0:
			if nums1 > nums2:
				result.append(nums1[0])
				nums1 = nums1[1:]
			else:
				result.append(nums2[0])
				nums2 = nums2[1:]
		return result


if __name__ == '__main__':

	print Solution().maxNumber([1,2],[],2)

	