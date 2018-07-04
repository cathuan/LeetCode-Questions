class Solution(object):

	def fullJustify(self, words, maxWidth):
		"""
		:type words: List[str]
		:type maxWidth: int
		:rtype: List[str]
		"""

		output = []

		currentWords = []
		currentLength = 0
		for i in range(len(words)):
			word = words[i]
			if currentLength + len(word) + len(currentWords) > maxWidth:
				spaceWidth = maxWidth - currentLength
				sentence = self.constructStringMiddle(currentWords, spaceWidth)
				output.append(sentence)
				currentWords = []
				currentLength = 0

			currentWords.append(word)
			currentLength += len(word)

		if len(currentWords) > 0:
			spaceWidth = maxWidth - currentLength - (len(currentWords)-1)
			sentence = self.constructStringEnd(currentWords, spaceWidth)
			output.append(sentence)

		return output

	def constructStringMiddle(self, words, spaceWidth):

		if len(words) == 1:
			return words + " " * spaceWidth

		m = spaceWidth / (len(words) - 1)
		r = spaceWidth % (len(words) - 1)

		segs = []
		for i in range(len(words)):
			word = words[i]
			segs.append(word)

			if i < r:
				segs.append(' '*(m+1))
			elif i < len(words) - 1:
				segs.append(' '*m)
			else:
				pass
		return ''.join(segs)

	def constructStringEnd(self, words, spaceWidth):
		return " ".join(words) + " " * spaceWidth


if __name__ == "__main__":

	print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)

	"justification.   "
	"justification.  "
	'justification.  '

