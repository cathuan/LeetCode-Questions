from collections import deque


class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        elif board[row][col] != "E":
            return board

        nrows = len(board)
        ncols = len(board[0])

        queue = deque()
        queue.append(click)
        seen = set()
        while queue:
            row, col = queue.popleft()
            count = 0
            surround = self.getSurround(nrows, ncols, row, col)
            for r, c in surround:
                if board[r][c] == "M":
                    count += 1

            if count > 0:
                board[row][col] = str(count)
            else:
                board[row][col] = "B"
                for r, c in surround:
                    if board[r][c] == "E" and (r, c) not in seen:
                        queue.append((r, c))
                        seen.add((r, c))

        return board

    def getSurround(self, nrows, ncols, row, col):
        ret = []
        for r in [row-1, row, row+1]:
            for c in [col-1, col, col+1]:
                if 0 <= r <= nrows-1 and 0 <= c <= ncols-1:
                    if (r, c) != (row, col):
                        ret.append((r, c))
        return ret
