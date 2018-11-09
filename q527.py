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

        for wordGroup in groups.itervalues():
            prefixTrie = Trie()
            for word, _ in wordGroup:
                prefixTrie.insert(word)

            for word, index in wordGroup:
                i = prefixTrie.search(word)
                length = len(word)-2 - i
                if length <= 1:
                    newWord = word
                else:
                    newWord = word[:i+1] + str(length) + word[-1]
                ret[index] = newWord
        return ret


if __name__ == "__main__":

    print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])