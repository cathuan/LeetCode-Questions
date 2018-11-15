import sys


class Solution(object):

	def countDigitOne(self, n):
		"""
		:type n: int
		:rtype: int
		"""
	
		if n <= 0:
			return 0

		# can't use log to find number of digits due to rounding error
		d = len(str(n)) - 1
		lead = n / (10 ** d)
		remain = n % (10 ** d)
		#print lead, remain, d

		count = 0
		if lead == 1:
			count += lead * d * (10 ** (d-1)) + remain + 1
		else:
			count += lead * d * (10 ** (d-1)) + 10 ** d
		count += self.countDigitOne(remain)
		return int(count)


if __name__ == '__main__':

	print Solution().countDigitOne(int(sys.argv[1]))