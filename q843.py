# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.wordsSimilarity = defaultdict(
            dict)  # word -> {similarity -> set(word)}

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """

        for i in range(len(wordlist)):
            word = wordlist[i]
            self.wordsSimilarity[word] = {}
            for j in range(0, len(wordlist)):
                otherWord = wordlist[j]
                similarity = sum(
                    [1 for a, b in zip(word, otherWord) if a == b])
                if similarity not in self.wordsSimilarity[word]:
                    self.wordsSimilarity[word][similarity] = set()
                self.wordsSimilarity[word][similarity].add(otherWord)

        potentialWords = set([word for word in wordlist])
        while len(potentialWords) > 0:
            word = potentialWords.pop()
            output = master.guess(word)
            if output == len(word):
                break
            potentialWords = potentialWords.intersection(
                self.wordsSimilarity[word][output])
