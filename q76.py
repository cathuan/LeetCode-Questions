class Solution(object):

	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""

		requiredCount = {}
		for char in t:
			if char not in requiredCount:
				requiredCount[char] = 0
			requiredCount[char] += 1

		meet = 0  # count of required chars in substring (don't count extra char if we exceed required amount)
		curStart = 0
		charCount = {}  # number of chars in t contained in substring curStart:curEnd+1
		seq = ''
		
		for curEnd in range(len(s)):
			char = s[curEnd]
			if char in t:
				if char not in charCount:
					charCount[char] = 0

				# don't count extra char if we exceed required amount
				if charCount[char] < requiredCount[char]:
					meet += 1
				charCount[char] += 1

			# shrink the left index to make sure required characters are all contained in sliding window
			if meet == len(t):
				while curStart < curEnd:
					# if we shrink one more char, the substring will not contain enough char (s[curStart])
					if s[curStart] in t and charCount[s[curStart]] == requiredCount[s[curStart]]:
						break
					if s[curStart] in t:
						charCount[s[curStart]] -= 1
					curStart += 1

				if len(seq) == 0 or len(seq) > curEnd - curStart + 1:
					seq = s[curStart:curEnd+1]
		return seq


if __name__ == "__main__":

	print Solution().minWindow("aa", "aa")

		