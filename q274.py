import numpy as np


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        if n == 0:
            return 0

        citations_counts = np.array([0]*(n+1))
        for citation in citations:
            if citation >= n:
                citations_counts[0] += 1
            else:
                citations_counts[n-citation] += 1

        #citations_cumsum = self.cumsum_reverse(citations_counts)
        citations_cumsum = citations_counts.cumsum()
        for index in range(n,-1,-1):
            # citations_cumsum[index] number of his paper
            # has at least index citation
            if citations_cumsum[index] <= n-index:
                if index == n:
                    return 0

                return max(n-index-1, citations_cumsum[index])


class Solution2(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        if n == 0:
            return 0

        citations_counts = [0]*(n+1)
        for citation in citations:
            if citation >= n:
                citations_counts[n] += 1
            else:
                citations_counts[citation] += 1

        citations_cumsum = self.cumsum_reverse(citations_counts)
        for index in range(n+1):
            # citations_cumsum[index] number of his paper
            # has at least index citation
            if citations_cumsum[index] <= index:
                break
        if index == 0:
            return 0

        return max(index-1, citations_cumsum[index])

    def cumsum_reverse(self, nums):

        result = [0] * len(nums)
        result[len(nums)-1] = nums[len(nums)-1]
        for i in xrange(len(nums)-2,-1,-1):
            result[i] = result[i+1] + nums[i]
        return result


class Solution3(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        if n == 0:
            return 0

        citations_counts = [0]*(n+1)
        for citation in citations:
            if citation >= n:
                citations_counts[n] += 1
            else:
                citations_counts[citation] += 1

        i = n-1
        while i >= 0:
            citations_counts[i] += citations_counts[i+1]
            if citations_counts[i+1] >= i+1:
                return i+1
            i -= 1
        return 0


if __name__ == "__main__":

    citations = np.random.randint(0,100000,50000)
    #print "["+",".join([str(c) for c in citations])+"]"
    print Solution().hIndex(citations)
    print Solution2().hIndex(citations)
