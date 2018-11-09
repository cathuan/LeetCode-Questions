class Solution(object):

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0

        nrows = len(matrix)
        ncols = len(matrix[0])

        maxLength = -1
        cache = {}
        for r in range(nrows):
            for c in range(ncols):
                ignore = False
                for r_, c_ in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    # outside of boundary
                    if r_ < 0 or r_ >= nrows or c_ < 0 or c_ >= ncols:
                        continue
                    if matrix[r_][c_] > matrix[r][c]:
                        ignore = True
                        break
                if ignore:
                    continue

                if (r,c) in cache:
                    maxLength = cache[(r,c)]
                else:
                    maxLength = max(maxLength, self.dfs(matrix, nrows, ncols, r, c, cache))
                    cache[(r,c)] = maxLength
                #print r, c, matrix[r][c], maxLength
        return maxLength

    def dfs(self, matrix, nrows, ncols, r, c, cache):
        if (r,c) in cache:
            return cache[(r,c)]

        val = matrix[r][c]
        maxLength = 1
        for r_, c_ in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            # outside of boundary
            if r_ < 0 or r_ >= nrows or c_ < 0 or c_ >= ncols:
                continue

            if matrix[r_][c_] >= val:
                continue

            length = self.dfs(matrix, nrows, ncols, r_, c_, cache)
            maxLength = max(maxLength, length+1)
            #print "**", r_, c_, matrix[r_][c_], length, maxLength
        cache[(r,c)] = maxLength
        return maxLength


if __name__ == "__main__":

    matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    print Solution().longestIncreasingPath(matrix)