import sys

class Solution(object):

	def calculate(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		seq = s
		tokens = []
		numSeq = ""
		for s in seq:
			if s == " ":
				continue
			if s.isdigit():
				numSeq += s
			else:
				if numSeq != "":
					tokens.append(int(numSeq))
				tokens.append(s)
				numSeq = ""
		if numSeq != "":
			tokens.append(int(numSeq))

		stack = []
		for token in tokens:
			if token == "(":
				stack.append(token)
			elif token == ")":
				n = stack.pop()
				stack.pop()
				stack.append(n)
			elif isinstance(token, int):
				stack.append(token)
			else:
				n = stack.pop()
				stack.append(token)
				stack.append(n)
			self.operate(stack)
			
		return int(stack[-1])

	def operate(self, stack):
		if len(stack) >= 3:
			if isinstance(stack[-1], int) and isinstance(stack[-2], int) and (stack[-3] in ["+", "-"]):
				n1 = stack.pop()
				n2 = stack.pop()
				op = stack.pop()
				if op == "+":
					stack.append(n2+n1)
				else:
					stack.append(n2-n1)
		return stack

if __name__ == '__main__':

	print Solution().calculate(sys.argv[1])
