class Solution(object):

    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 4

        k = 2
        for t in range(3, target+1):
            if t == 2 ** k - 1:
                dp[t] = k
                k += 1
                continue

            min_step = float('inf')
            for j in range(k-1):
                min_step = min(min_step, k-1+1+j+1+dp[t-2**(k-1)+2**j])
            min_step = min(min_step, k+1+dp[2**k-1-t])
            dp[t] = min_step
        return dp[target]


if __name__ == "__main__":
    print Solution().racecar(3)