class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        dp = []
        for i in range(len(word1) + 1):
            dp.append([0] * (len(word2) + 1))

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i - 1][j - 1] + 1,
                                   dp[i][j - 1] + 1)

        return dp[len(word1)][len(word2)]
