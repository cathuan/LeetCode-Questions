from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.count = defaultdict(int)
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
            node.count[(word[-1], len(word))] += 1

    def search(self, word):
        node = self.root
        for i, w in enumerate(word):
            assert w in node.children
            node = node.children[w]
            if node.count[(word[-1], len(word))] == 1:
                break
        else:
            assert False, word
        return i


class Solution(object):

    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """

        prefixTrie = Trie()
        for word in dict:
            prefixTrie.insert(word)

        ret = []
        for word in dict:
            i = prefixTrie.search(word)
            length = len(word)-2 - i
            if length <= 1:
                newWord = word
            else:
                newWord = word[:i+1] + str(length) + word[-1]
            ret.append(newWord)
        return ret


if __name__ == "__main__":

    print Solution().wordsAbbreviation(["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"])