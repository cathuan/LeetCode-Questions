class Solution(object):

	@profile
	def maxNumber(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""

		dp = {}

		stack = []
		stack.append((len(nums1), len(nums2), k))
		while len(stack) > 0:

			if stack[-1] in dp:
				stack.pop()
				continue
			n1, n2, k_ = stack[-1]
			#print n1, n2, k_, stack[-1]

			if k_ == 0:
				dp[(n1, n2, k_)] = []
				stack.pop()
				continue

			nums1_ = nums1[-n1:] if n1 != 0 else []
			nums2_ = nums2[-n2:] if n2 != 0 else []

			length = len(nums1_) + len(nums2_) - k + 1
			maxIndex1 = self.findMax(nums1_, length)
			maxIndex2 = self.findMax(nums2_, length)
			#print "***", maxIndex1, maxIndex2, len(nums1_), len(nums2_)

			maxValue1 = nums1_[maxIndex1] if maxIndex1 is not None else float("-inf")
			maxValue2 = nums2_[maxIndex2] if maxIndex2 is not None else float("-inf")

			if maxValue1 == maxValue2:
				needContinue = False
				if (len(nums1_[maxIndex1+1:]), len(nums2_), k_-1) not in dp:
					stack.append((len(nums1_[maxIndex1+1:]), len(nums2_), k_-1))
					needContinue = True
				if (len(nums1_), len(nums2_[maxIndex2+1:]), k_-1) not in dp:
					stack.append((len(nums1_), len(nums2_[maxIndex2+1:]), k_-1))
					needContinue = True
				if needContinue:
					continue
				r = max(dp[(len(nums1_[maxIndex1+1:]), len(nums2_), k_-1)], dp[(len(nums1_), len(nums2_[maxIndex2+1:]), k_-1)])
				r.insert(0, maxValue1)
			elif maxValue1 > maxValue2:
				if (len(nums1_[maxIndex1+1:]), len(nums2_), k_-1) not in dp:
					stack.append((len(nums1_[maxIndex1+1:]), len(nums2_), k_-1))
					continue
				r = dp[(len(nums1_[maxIndex1+1:]), len(nums2_), k_-1)]
				r.insert(0,maxValue1)
			else:
				if (len(nums1_), len(nums2_[maxIndex2+1:]), k_-1) not in dp:
					stack.append((len(nums1_), len(nums2_[maxIndex2+1:]), k_-1))
					continue
				r = dp[(len(nums1_), len(nums2_[maxIndex2+1:]), k_-1)]
				r.insert(0, maxValue2)
			stack.pop()
			#print "ahahah", n1, n2, k_, len(nums1_), len(nums2_)
			dp[(len(nums1_), len(nums2_), k_)] = r
		return dp[(len(nums1), len(nums2), k)]

	# Find the index of max value in nums[:k]. If there are multiple max value, we return the first index.
	def findMax(self, nums, k):
		if len(nums) == 0:
			return None

		maxIndex = 0
		for i in range(1, min(k, len(nums))):
			if nums[i] > nums[maxIndex]:
				maxIndex = i
		return maxIndex


if __name__ == '__main__':

	print Solution().maxNumber([1,2,0,1,1,2,1,0,2,0,2,1,1,1,1,0,0,2,0,0,2,1,2,1,0,1,1,0,1,2,1,0,2,0,0,1,0,1,2,0,0,0,1,1,2,1,1,1,0,0,0,0,1,2,1,2,1,1,1,2,2,2,1,2,2,0,2,0,0,0,2,1,0,2,2,0,0,2,2,2,0,2,2,2,1,1,0,0,2,1,1,1,0,1,1,1,1,2,1,0,0,1,1,1,2,1,1,1,0,0,0,2,2,2,1,2,0,0,1,1,2,1,1,1,1,1,0,2,2,2,0,2,2,0,1,1,1,1,2,0,2,2,1,0,2,0,1,0,1,2,0,0,0,0,2,2,2,2,2,1,1,0,1,2,2,2,1,2,0,0,1,2,2,1,1,1,1,0,1,0,1,1,0,0,2,2,1,2,1,2,0,0,2,0,2,1,1,1,2,0,0,1,1,1,2,1,1,1,2,2,1,2,2,2,0,0,2,2,0,1,0,0,0,1,1,2,2,2,0,0,1,2,0,0,2,2,1,0,2,1,0,0,0,0,1,0,2,1,0,1,2,1,1,0,1,2,1,2,0,1,1,2,1,1,0,1,0,1,1,1,1,1,0,1,0,0,0,1,2,0,2,2,0,2,1,0,2,1,0,0,0,2,2,2,0,1,1,1,2,0,2,1,0,2,2,0,1,1,0,1,2,2,0,2,2,0,1,0,2,0,1,1,1,0,1,2,2,0,1,0,2,0,2,0,2,0,2,0,2,2,1,1,0,0,0,2,2,1,1,2,1,2,0,2,0,1,0,1,1,0,0,0,2,1,0,0,1,1,0,1,0,0,1,1,0,1,1,2,0,0,0,1,1,2,2,2,2,2,1,1,1,0,0,1,0,0,2,1,2,2],
							   [2,1,2,1,0,0,0,1,2,1,0,1,1,2,1,2,1,1,2,0,0,0,1,0,1,0,2,0,1,2,0,2,0,1,2,0,1,0,0,0,1,0,1,1,1,2,2,2,1,2,1,0,2,0,0,2,0,2,0,1,2,1,0,1,1,2,0,0,2,0,2,2,2,2,1,2,1,2,1,1,0,0,1,2,2,2,1,1,1,1,1,0,1,0,0,1,1,1,0,0,2,0,1,1,1,2,1,1,0,0,0,0,1,1,1,2,0,2,2,2,0,2,2,0,1,2,0,1,0,0,1,1,0,1,2,0,1,1,2,2,1,1,0,2,1,0,2,2,0,1,2,1,1,2,1,0,2,2,1,1,1,1,1,2,1,1,0,2,0,2,2,0,2,1,0,0,1,0,0,0,2,2,2,0,2,2,0,0,1,1,1,0,0,2,2,1,1,2,0,1,0,2,1,1,1,0,1,2,0,2,2,1,1,0,0,2,1,1,2,1,1,0,1,1,0,2,1,0,2,2,2,1,0,1,2,1,0,2,1,1,1,1,1,2,1,0,2,1,0,2,2,2,1,1,2,1,1,1,2,2,0,0,2,0,0,0,2,2,2,1,2,2,2,2,2,0,1,1,0,2,1,2,2,2,1,0,2,2,2,0,1,1,0,1,1,0,2,1,1,2,1,0,2,2,1,2,2,0,1,1,2,1,0,0,2,2,2,1,2,1,0,1,1,2,0,2,0,0,2,0,2,0,0,1,0,0,1,0,1,0,2,2,1,1,2,0,2,1,2,0,1,2,1,0,0,2,1,2,2,1,0,0,2,2,1,2,2,1,1,2,0,2,1,2,2,1,0,1,2,0,1,0,1,1,0,2,0,1,2,2,1,2,0,1,2,0,1,1,0,2],
							   800)