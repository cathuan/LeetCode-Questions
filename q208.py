from collections import defaultdict


class TrieNode(object):

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


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
        pass

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pass

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pass


if __name__ == "__main__":

    trie = Trie()
    print trie.search("apple")
    trie.insert("apple")
    print trie.search("apple")
    print trie.search("app")
    print trie.startsWith("app")
    trie.insert("app")
    print trie.search("app")

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)