class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if k >= len(prices)/2:
            return self.quickSolve(prices)

        dp = []
        for _ in range(k+1):
            dp.append([0]*len(prices))

        # dp[i][j] = maximum pnl for at most i trades up to day j
        for i in range(1, k+1):
            lastTrade = prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] - lastTrade)
                lastTrade = min(lastTrade, prices[j] - dp[i-1][j-1])

        return dp[k][len(prices)-1]

    def quickSolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":

    print Solution().maxProfit(2, [2, 4, 1])
