from collections import defaultdict, deque


class TrieNode(object):

    def __init__(self):
        self.word = None
        self.freq = 0
        self.isWord = False
        self.children = defaultdict(TrieNode)


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word, freq):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            w = word[i]
            node = node.children[w]
            node.word = word[:i+1]
        if node.isWord:
            node.freq += freq
        else:
            node.isWord = True
            node.freq += freq

    def searchStartsWith(self, prefix):
        node = self.root
        for w in prefix:
            if w not in node.children:
                return []  # no historical usage
            node = node.children[w]
        return self.expand(node)

    def expand(self, node):
        stack = deque()
        stack.append(node)

        ret = []
        while stack:
            node = stack.popleft()
            if node.isWord:
                ret.append(node)
            for node_ in node.children.values():
                assert node_.word is not None
                stack.append(node_)

        ret = sorted(ret, key=(lambda node: (-node.freq, node.word)))
        ret = [node.word for node in ret]
        if len(ret) > 3:
            return ret[:3]
        else:
            return ret


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)
        self.currentInput = ''

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.trie.insert(self.currentInput, 1)
            self.currentInput = ""
            return []

        self.currentInput += c
        return self.trie.searchStartsWith(self.currentInput)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


if __name__ == "__main__":

    completion = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
    print completion.input("i")
    print completion.input(" ")
    print completion.input("#")
    print completion.input("i")
    print completion.input(" ")
    print completion.input("a")
    print completion.input("#")
    print completion.input("i")
    print completion.input(" ")
    print completion.input("a")
    print completion.input("#")