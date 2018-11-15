class Solution(object):

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

        for r in range(nRows):
            for c in range(nCols):
                if self.isValid(board, r, c, 0, word, set(), nRows, nCols):
                    return True
        return False

    def isValid(self, board, r, c, i, word, seen, nRows, nCols):
        if board[r][c] != word[i]:
            return False

        if i == len(word)-1 and board[r][c] == word[i]:
            return True

        seen.add((r,c))
        for x, y in [(r+1, c), (r-1,c), (r,c+1), (r, c-1)]:
            if x < 0 or x >= nRows or y < 0 or y >= nCols:
                continue
            if (x,y) in seen:
                continue

            seen.add((x,y))
            if self.isValid(board, x, y, i+1, word, seen, nRows, nCols):
                return True
            seen.remove((x,y))

        return False

if __name__ == "__main__":

    board = [["a","b","b","b","b","b","b","a"],["a","a","a","b","b","b","a","b"],["a","b","b","b","a","b","a","a"],["b","a","a","b","b","b","a","a"],["a","b","b","b","a","b","b","b"],["b","b","a","a","a","a","b","a"],["b","a","a","b","a","a","a","b"],["a","a","a","b","b","a","b","b"],["b","b","a","a","a","b","b","b"],["a","b","b","a","b","b","b","a"]]
    word = "babbaabaaabaa"
    print Solution().exist(board, word)
