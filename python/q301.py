# -*- coding: utf-8 -*

import sys


# 因为要求去掉最少的element，所以我们用BFS更简单，可以提前结束：开始见到一个答案以后，就不会再继续走下一层了。
# BFS的话我们用queue来存数据。
class Solution(object):

	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""

		queue = []
		seen_str = set()
		result = []
		get_min_length = False

		queue.append(s)
		while len(queue) > 0:

			current = queue.pop(0)

			# if the current string is valid, simply push it in the result and continue to the next step.
			if self.isValid(current) and current not in result:
				get_min_length = True
				result.append(current)
				continue

			if get_min_length:
				continue

			for i in range(len(current)):
				if current[i] not in ['(', ')']:
					continue
				new = current[:i] + current[i+1:]
				if new not in seen_str:
					stack.append(new)
					seen_str.add(new)

		return result

	# 用一个简单的stack来判断。注意当)过多的时候stack有可能变成空的，需要特别处理一下。
	def isValid(self, str):
		stack = []
		for s in str:
			if s == "(":
				stack.append(s)
			elif s == ")":
				if len(stack) == 0:
					return False
				stack.pop()
		return len(stack) == 0


if __name__ == "__main__":

	print Solution().removeInvalidParentheses(sys.argv[1])