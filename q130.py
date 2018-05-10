# Ugly code...
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = len(board)
        if n == 0:
            return
        m = len(board[0])
        if m == 0:
            return

        convertible = self.record_edges(n, m)

        while len(convertible) > 0:
            i, j = convertible.pop()
            if board[i][j] == "A":
                continue
            board[i][j] = "A"

            right_index = self.get_right(i,j,n,m)
            left_index = self.get_left(i,j,n,m)
            above_index = self.get_above(i,j,n,m)
            below_index = self.get_below(i,j,n,m)

            if right_index is not None:
                a, b = right_index
                if board[a][b] == "O":
                    convertible.append(right_index)
            if left_index is not None:
                a, b = left_index
                if board[a][b] == "O":
                    convertible.append(left_index)
            if above_index is not None:
                a, b = above_index
                if board[a][b] == "O":
                    convertible.append(above_index)
            if below_index is not None:
                a, b = below_index
                if board[a][b] == "O":
                    convertible.append(below_index)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "A":
                    board[i][j] = "O"

    def record_edges(self, n, m):
        convertible = []

        for j in range(m):
            if board[0][j] == "O":
                convertible.append((0,j))
            if board[n-1][j] == "O":
                convertible.append((n-1,j))
        for i in range(n):
            if board[i][0] == "O":
                convertible.append((i,0))
            if board[i][m-1] == "O":
                convertible.append((i,m-1))
        return convertible

    def get_right(self, i, j, n, m):
        if j == m-1:
            return None
        else:
            return (i, j+1)

    def get_left(self, i, j, n, m):
        if j == 0:
            return None
        else:
            return (i, j-1)

    def get_above(self, i, j, n, m):
        if i == 0:
            return None
        else:
            return (i-1, j)

    def get_below(self, i, j, n, m):
        if i == n-1:
            return None
        else:
            return (i+1, j)


if __name__ == "__main__":

    print Solution().solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])
