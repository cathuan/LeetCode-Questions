from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.count = 0
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            w = word[i]
            node = node.children[w]
            node.count += 1

    def search(self, word):
        node = self.root
        for i, w in enumerate(word):
            assert w in node.children
            node = node.children[w]
            if node.count == 1:
                break
        else:
            assert False, word
        return i


class Solution(object):

    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        ret = [None] * len(words)

        groups = defaultdict(list)
        for word, index in sorted([(word, index) for index, word in enumerate(words)]):
            groups[(word[0], word[-1], len(word))].append((word, index))

        for wordGroup in groups.values():
            wordGroup = sorted(wordGroup)
            for index, (word, origIndex) in enumerate(wordGroup):
                maxIndex = 1
                if index >= 1:
                    curMaxIndex = self.compare(wordGroup[index-1][0], word)
                    maxIndex = max(maxIndex, curMaxIndex+1)
                if index <= len(wordGroup)-2:
                    curMaxIndex = self.compare(wordGroup[index+1][0], word)
                    maxIndex = max(maxIndex, curMaxIndex+1)
                length = len(word) - 1 - maxIndex
                if length <= 1:
                    newWord = word
                else:
                    newWord = word[:maxIndex] + str(length) + word[-1]
                ret[origIndex] = newWord

        return ret

    def compare(self, word1, word2):
        for index, (w1, w2) in enumerate(zip(word1, word2)):
            #print "???", w1, w2, word1, word2
            if w1 != w2:
                return index


if __name__ == "__main__":

    print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])