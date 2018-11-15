from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.char = None
        self.weights = -1
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word, weight):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        #print "insert", word
        node = self.root
        for i in range(len(word)):
            w = word[i]
            node = node.children[w]
            node.char = w
            node.weights = max(node.weights, weight)

    def searchStartsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w not in node.children:
                return -1
            node = node.children[w]
        return node.weights


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.trie = Trie()
        for weight, word in enumerate(words):
            newWord = word[::-1]
            word = "#" + word
            self.trie.insert(word, weight)
            for w in newWord:
                word = w + word
                #print w, newWord, word
                self.trie.insert(word, weight)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """

        letters = suffix + "#" + prefix
        return self.trie.searchStartsWith(letters)


if __name__ == "__main__":

    wf = WordFilter(["apple"])
    print wf.f("a", "e")


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
