import sys


class Solution(object):

	def __init__(self):

		self.buffer = {"1": "One",
					   "2": "Two",
					   "3": "Three",
					   "4": "Four",
					   "5": "Five",
					   "6": "Six",
					   "7": "Seven",
					   "8": "Eight",
					   "9": "Nine",
					   "10": "Ten",
					   "11": "Eleven",
					   "12": "Twelve",
					   "13": "Thirteen",
					   "14": "Fourteen",
					   "15": "Fifteen",
					   "16": "Sixteen",
					   "17": "Seventeen",
					   "18": "Eighteen",
					   "19": "Nineteen"
					  }
		self.tens = {"2": "Twenty",
					 "3": "Thirty",
					 "4": "Forty",
					 "5": "Fifty",
					 "6": "Sixty",
					 "7": "Seventy",
					 "8": "Eighty",
					 "9": "Ninety"
					}

		self.order = {0: None,
					  1: "Thousand",
					  2: "Million",
					  3: "Billion",
					  4: "Trillion"}

	def numberToWords(self, num):
		"""
		:type num: int
		:rtype: str
		"""

		if num == 0:
			return "Zero"
		
		num = str(num)
		count = 0
		result = ""
		while len(num) > 0:
			if len(num) >= 3:
				cur = num[-3:]
				num = num[:-3]
			else:
				cur = num
				num = ""

			order = self.order[count]
			threeDigit = self.getThreeDigits(cur)
			if threeDigit == "":
				pass
			else:
				if order is None:
					result = threeDigit
				else:
					if result != "":
						result = threeDigit + " " + order + " " + result
					else:
						result = threeDigit + " " + order
			count += 1
		return result

	def getThreeDigits(self, s):
		assert len(s) <= 3

		if len(s) == 1:
			if s != "0":
				return self.buffer[s]
		elif len(s) == 2:
			return self.getTwoDigits(s)
		else:
			if s[0] != "0":
				twoDigit = self.getTwoDigits(s[1:])
				if twoDigit != "":
					return self.buffer[s[0]] + " " + "Hundred" + " " + twoDigit
				else:
					return self.buffer[s[0]] + " Hundred"
			else:
				return self.getTwoDigits(s[1:])

	def getTwoDigits(self, s):
		assert len(s) == 2

		if s[0] == "0":
			if s[1] != "0":
				return self.buffer[s[1]]
			else:
				return ""
		elif s[0] == "1":
			return self.buffer[s]
		else:
			if s[1] != "0":
				return self.tens[s[0]] + " " + self.buffer[s[1]]
			else:
				return self.tens[s[0]]


if __name__ == '__main__':
	print Solution().numberToWords(sys.argv[1])