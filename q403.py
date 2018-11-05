from collections import defaultdict


class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        # distance -> [step]
        dp = defaultdict(set)
        dp[0].add(0)

        for distance in stones:
            for step in dp[distance]:
                if step > 1:
                    dp[distance + step - 1].add(step - 1)
                dp[distance + step].add(step)
                dp[distance + step + 1].add(step + 1)

        return len(dp[stones[-1]]) > 0


if __name__ == "__main__":

    print Solution().canCross([0, 1, 2, 3, 4, 8, 9, 11])
