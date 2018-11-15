import collections


class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True


class Solution(object):

    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root

        # construct trie with words
        for w in words:
            trie.insert(w)

        # use dfs to search all possible words constructed by board.
        # if one of the word is stored in trie, append it in the res.
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, node, i, j, "", res)

        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False

        # return if the cell is outside of the board
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp


if __name__ == "__main__":
    board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"],
             ["a", "b", "a", "a", "a", "b"], ["a", "b", "a", "b", "b", "a"],
             ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
             ["a", "a", "b", "a", "a", "b"]]
    words = ["aabbbbabbaababaaaabababbaaba"]

    print Solution().findWords(board, words)
