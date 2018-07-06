import sys

class Solution(object):

	def minCut(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		isPalindrome = [[False] * len(s) for _ in range(len(s))]
		for i in range(len(s)):
			isPalindrome[i][i] = True

		cuts = range(1,len(s)+1)
		for j in range(len(s)):
			for i in range(j+1):
				if s[i] == s[j] and (j - i < 2 or isPalindrome[i+1][j-1]):
					isPalindrome[i][j] = True
					if i == 0:
						cuts[j] = 0
					else:
						cuts[j] = min(cuts[j], cuts[i-1]+1)
		return cuts[-1]


if __name__ == '__main__':

	print Solution().minCut(sys.argv[1])