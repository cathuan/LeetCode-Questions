from collections import defaultdict


class Node(object):

    def __init__(self, char, row, col):
        self.char = char
        self.children = defaultdict(list)
        self.row = row
        self.col = col


class Board(object):

    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = 0 if self.rows == 0 else len(board[0])
        self.nodes = {}

        for r in range(self.rows):
            for c in range(self.cols):
                self.insert(r, c)

    def getNeighbour(self, row, col):
        neighbours = []
        for row_, col_ in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            if 0 <= row_ <= self.rows-1 and 0 <= col_ <= self.cols-1:
                neighbours.append((row_, col_))
        return neighbours

    def getNode(self, row, col):
        if (row, col) not in self.nodes:
            char = self.board[row][col]
            node = Node(char, row, col)
            self.nodes[(row, col)] = node
        return self.nodes[(row, col)]

    def insert(self, row, col):
        nodeInsert = self.getNode(row, col)
        for r, c in self.getNeighbour(row, col):
            node = self.getNode(r, c)
            node.children[nodeInsert.char].append(nodeInsert)
            nodeInsert.children[node.char].append(node)

    def query(self, word):
        if len(word) == 0:
            return False

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == word[0]:
                    node = self.getNode(r, c)
                    seen = set()
                    seen.add((node.row, node.col))
                    for i in range(1, len(word)):
                        char = word[i]
                        #print "*", i, char
                        if char in node.children:
                            for curNode in node.children[char]:
                                if (curNode.row, curNode.col) not in seen:
                                    node = curNode
                                    seen.add((node.row, node.col))
                                    #print node.row, node.col, node.char
                                    break
                            else:
                                break
                        else:
                            break
                    else:
                        return True
        return False


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        b = Board(board)
        ret = []
        for word in words:
            if b.query(word) and word not in ret:
                ret.append(word)
        return ret


if __name__ == "__main__":
    board = [['a','a']
    ]
    words = ['aaa']

    print Solution().findWords(board, words)
