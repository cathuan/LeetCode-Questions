import sys


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]

        dp[0][0] = True
        for i in range(1, len(p)+1):
        	if p[i-1] == "*":
        		dp[0][i] = True
        	else:
        		break

        for i in range(1,len(s)+1):
        	for j in range(1,len(p)+1):
        		if p[j-1] == "?" or p[j-1] == s[i-1]:	
        			dp[i][j] = dp[i-1][j-1]
        		elif p[j-1] == "*":
        			dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]

        return dp[len(s)][len(p)]

if __name__ == '__main__':

	print Solution().isMatch(sys.argv[1], sys.argv[2])

