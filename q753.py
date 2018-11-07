class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seen = set()
        start = "0"*(n-1)
        ans = self.dfs(seen, start, k)
        return "".join(ans) + start

    def dfs(self, seen, start, k):
        ans = []
        for i in range(k):
            node = start + str(i)
            if node not in seen:
                seen.add(node)
                ans.extend(self.dfs(seen, node[1:], k))
                ans.append(str(i))
        return ans


if __name__ == "__main__":

    print Solution().crackSafe(2,2)