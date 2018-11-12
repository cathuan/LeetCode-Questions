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

        meet = 0
        charCount = {}
        seq = ''

		# using curStart and curEnd as two pointers shrinking the subarray
        curStart = 0
        for curEnd in range(len(s)):
            char = s[curEnd]
            if char in t:
                if char not in charCount:
                    charCount[char] = 0
                if charCount[char] < requiredCount[char]:
                    meet += 1
                charCount[char] += 1

            if meet == len(t):
                while curStart < curEnd:
                    if s[curStart] in t and \
						charCount[s[curStart]] == requiredCount[s[curStart]]:
                        break
                    if s[curStart] in t:
                        charCount[s[curStart]] -= 1
                    curStart += 1

				# resulting sequence is buffered if it's shorter
                if len(seq) == 0 or len(seq) > curEnd - curStart + 1:
                    seq = s[curStart:curEnd + 1]
        return seq
