class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    for v in range(1, 10):
                        v = str(v)
                        if self.isValid(board, row, col, v):
                            board[row][col] = v

                            if self.solve(board):
                                return True
                        board[row][col] = '.'
                    return False
        return True

    def isValid(self, board, row, col, v):
        assert isinstance(v, str)
        for r, c in self.findRelatedCells(row, col):
            if board[r][c] == '.':
                continue
            if board[r][c] == v:
                return False
        return True

    def findRelatedCells(self, row, col):
        cells = set()
        for c in range(9):
            cells.add((row, c))
        for r in range(9):
            cells.add((r, col))

        rCell, cCell = row//3*3, col//3*3
        for r in range(3):
            for c in range(3):
                cells.add((rCell+r, cCell+c))
        return cells


if __name__ == "__main__":

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    for row in board:
        print row
    print
    Solution().solveSudoku(board)

    for row in board:
        print row

    solution = [["5", "1", "9", "7", "4", "8", "6", "3", "2"], ["7", "8", "3", "6", "5", "2", "4", "1", "9"], ["4", "2", "6", "1", "3", "9", "8", "7", "5"], ["3", "5", "7", "9", "8", "6", "2", "4", "1"], ["2", "6", "4",
                                                                                                                                                                                                             "3", "1", "7", "5", "9", "8"], ["1", "9", "8", "5", "2", "4", "3", "6", "7"], ["9", "7", "5", "8", "6", "3", "1", "2", "4"], ["8", "3", "2", "4", "9", "1", "7", "5", "6"], ["6", "4", "1", "2", "7", "5", "9", "8", "3"]]

    print
    for row in solution:
        print row
