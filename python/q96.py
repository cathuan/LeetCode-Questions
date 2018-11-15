class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        results = {}

        for k in range(n+1):
            if k == 0:
                result = 1
            elif k == 1:
                result = 1
            else:
                result = 0
                for j in range(k):
                    left = j
                    right = k-1-j
                    result += results[left] * results[right]
            results[k] = result
        print results
        return results[n]
       

if __name__ == "__main__":

    print Solution().numTrees(0)
