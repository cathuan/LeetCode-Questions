import sys


class Solution(object):

	def removeInvalidParentheses(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""

		stack = []
		seen_str = set()
		result = []
		get_min_length = False

		stack.append(s)
		while len(stack) > 0:

			current = stack.pop(0)

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