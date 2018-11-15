class Solution(object):

    diffs = {}

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if self.diffCharCount(beginWord, endWord) == 1:
            return 1

        min_step = None
        for word in wordList:
            if self.diffCharCount(beginWord, word) == 1:
                if min_step is None:
                    min_step = self.ladderLength(word, endWord, wordList) + 1
                else:
                    min_step = min(self.ladderLength(word, endWord, wordList) + 1, min_step)
        return min_step

    def diffCharCount(self, word1, word2):

        if (word1, word2) in Solution.diffs:
            return Solution.diffs[(word1, word2)]

        if (word2, word1) in Solution.diffs:
            return Solution.diffs[(word2, word1)]

        count = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                count += 1

        Solution.diffs[(word1, word2)] = count
        return count
