# Really inefficient. Need to check better solutions.
# https://leetcode.com/problems/minimum-window-subsequence/solution/
class Solution(object):

    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        # special case do_something

        dp = []
        for _ in range(len(T)):
            dp.append([None] * len(S))

        # populate the first row
        char = T[0]
        for j in range(len(S)):
            if j == 0:
                if S[0] == char:
                    dp[0][j] = 1
                else:
                    continue
            else:
                if S[j] == char:
                    dp[0][j] = 1
                elif dp[0][j-1] is not None:
                    dp[0][j] = dp[0][j - 1] + 1
                else:
                    continue

        # populate the rest of the matrix
        for i in range(1, len(T)):
            for j in range(len(S)):
                if i > j:
                    continue

                if dp[i - 1][j - 1] is None:
                    continue

                if dp[i][j - 1] is None:
                    if dp[i - 1][j - 1] is not None and T[i] == S[j]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        continue
                else:
                    if T[i] == S[j]:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1

        min_count = float('inf')
        w = ''
        for i in range(len(S)):
            if dp[-1][i] is not None and dp[-1][i] < min_count:
                min_count = dp[-1][i]
                w = S[i + 1 - dp[-1][i]:i + 1]
        return w


if __name__ == "__main__":

    print Solution().minWindow("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u")