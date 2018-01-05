class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        result_list = self.getListResult(n, k)
        return "".join([str(val) for val in result_list])

    def getListResult(self, n, k):

        if k == 1:
            return range(1, n+1)

        step = self.factorial(n-1)
        count = 1
        while k > step:
            k -= step
            count += 1

        prev_list = self.getListResult(n-1, k)
        result = [count]
        for val in prev_list:
            if val < count:
                result.append(val)
            else:
                result.append(val+1)

        return result

    def factorial(self, n):

        if n == 1:
            return 1
        return n * self.factorial(n-1)
