# A naive DFS solution which passes the test with low efficiency.
# There should be a better solution.


class Solution(object):
    def __init__(self):
        self.debt = []

    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balance = {}
        for t in transactions:
            if t[0] not in balance:
                balance[t[0]] = 0
            if t[1] not in balance:
                balance[t[1]] = 0

            balance[t[0]] -= t[2]
            balance[t[1]] += t[2]

        for _, bal in balance.items():
            if bal != 0:
                self.debt.append(bal)

        return self.dfs(0, 0)

    def dfs(self, s, cnt):
        while s < len(self.debt) and self.debt[s] == 0:
            s += 1

        res = 2e19
        prev = 0
        for i in range(s + 1, len(self.debt)):
            if self.debt[i] != prev and self.debt[i] * self.debt[s] < 0:
                self.debt[i] += self.debt[s]
                res = min(res, self.dfs(s + 1, cnt + 1))
                self.debt[i] -= self.debt[s]
                prev = self.debt[i]
        if res < 2e18:
            return res
        else:
            return cnt
