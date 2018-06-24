import sys


class Solution(object):

	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		max_len = 0

		stack = [-1]
		for i in range(len(s)):
			token = s[i]
			if token == "(":
				stack.append(i)
			else:
				j = stack.pop()
				if len(stack) == 0:
					stack.append(i)
				else:
					cur_len = i - stack[-1]
					max_len = max(max_len, cur_len)
		return max_len


if __name__ == "__main__":

	s = sys.argv[1]
	print Solution().longestValidParentheses(s)