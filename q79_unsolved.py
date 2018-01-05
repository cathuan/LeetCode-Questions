import copy

# need to use DFS instead of BFS

class SolutionBFS(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        nRows = len(board)
        if nRows == 0:
            return False
        nCols = len(board[0])
        if nCols == 0:
            return False

        result = self.returnPath(nRows, nCols, board, word)
        return len(result) > 0

    def returnPath(self, nRows, nCols, board, word):

        if len(word) == 1:
            result = []
            for i in range(nRows):
                for j in range(nCols):
                    if board[i][j] == word:
                        result.append([(i,j)])
            return result

        result = []
        prev_result = self.returnPath(nRows, nCols, board, word[:-1])
        for path in prev_result:
            i, j = path[-1]
            if i > 0 and (i-1,j) not in path and board[i-1][j] == word[-1]:
                new_path = copy.copy(path)
                new_path.append((i-1,j))
                result.append(new_path)
            if i < nRows-1 and (i+1,j) not in path and board[i+1][j] == word[-1]:
                new_path = copy.copy(path)
                new_path.append((i+1,j))
                result.append(new_path)
            if j > 0 and (i,j-1) not in path and board[i][j-1] == word[-1]:
                new_path = copy.copy(path)
                new_path.append((i,j-1))
                result.append(new_path)
            if j < nCols-1 and (i,j+1) not in path and board[i][j+1] == word[-1]:
                new_path = copy.copy(path)
                new_path.append((i,j+1))
                result.append(new_path)
        return result


if __name__ == "__main__":

    board = [["a","b","b","b","b","b","b","a"],["a","a","a","b","b","b","a","b"],["a","b","b","b","a","b","a","a"],["b","a","a","b","b","b","a","a"],["a","b","b","b","a","b","b","b"],["b","b","a","a","a","a","b","a"],["b","a","a","b","a","a","a","b"],["a","a","a","b","b","a","b","b"],["b","b","a","a","a","b","b","b"],["a","b","b","a","b","b","b","a"]]
    word = "babbaabaaabaa"
    print Solution().exist(board, word)
