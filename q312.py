# -*- coding: utf-8 -*


# 这里我们用了interval dp，是一种比较基本的算法。
class Solution(object):

	def maxCoins(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums = [1] + nums + [1]
		n = len(nums)

		# dp[i][j]存的是如果我们戳掉全部[i+1,i+2,\ldots,j-1]的气球以后得到的最好的分数。
		dp = [[0] * n for _ in xrange(n)]

		for k in range(1, n):
			for i in range(n-k):
				j = i + k
				if k == 1:
					continue
				coins = 0
				for m in range(i+1, j):
					# m是i+1 .. j-1 这个列中最后一个被戳掉的气球
					coins = max(coins, nums[i] * nums[m] * nums[j] + dp[i][m] + dp[m][j])
				dp[i][j] = coins

		return dp[0][n-1]


if __name__ == '__main__':
	print Solution().maxCoins([1,2])