from collections import deque
import copy


class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        sol = [[1, 2, 3], [4, 5, 0]]
        if board == sol:
            return 0

        # board, count, row, col
        queue = deque()
        for r in range(2):
            for c in range(3):
                if board[r][c] == 0:
                    queue.append((board, 0, r, c))
        visited = {}
        visited[self.transform(board)] = 0

        while queue:
            board, count, r, c = queue.popleft()
            newCount = count + 1
            for row, col in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if row < 0 or row >= 2 or col < 0 or col >= 3:
                    continue
                newBoard = copy.deepcopy(board)
                newBoard[r][c], newBoard[row][col] = newBoard[row][col], newBoard[r][c]
                if newBoard == sol:
                    return newCount
                key = self.transform(newBoard)
                if key not in visited or newCount < visited[key]:
                    visited[key] = newCount
                    queue.append((newBoard, newCount, row, col))
        return -1

    def transform(self, board):
        ret = board[0] + board[1]
        return tuple(ret)
