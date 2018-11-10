# Some solution/explanation:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/135704/Detail-explanation-of-DP-solution


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        if k >= len(prices)/2:
            return self.quickSolve(prices)

        # here the memory is not so efficient.
        # should use O(n) instead of O(kn)
        dp = []
        for _ in range(k+1):
            dp.append([0]*len(prices))

        # dp[i][j] = maximum pnl for at most i trades up to day j
        # dp[0][j] = 0
        # dp[i][j] =
        #   max(dp[i][j-1],  # not trade on the day i
        #       dp[i-1][k-1] + prices[j] - prices[k] for k = 0..j-1)  # last trade on day k to j
        for i in range(1, k+1):
            lastTrade = prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j-1], prices[j] - lastTrade)
                lastTrade = min(lastTrade, prices[j] - dp[i-1][j-1])

        return dp[k][len(prices)-1]

    # when k >= len(prices)/2, then maximize profits since the number of
    # trading opportunities is sufficient. This is faster and avoid
    # memory usage when k is large.
    def quickSolve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit


if __name__ == "__main__":

    print Solution().maxProfit(2, [2, 4, 1])
