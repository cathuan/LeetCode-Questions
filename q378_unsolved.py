class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """


if __name__ == "__main__":

    matrix = [
       [ 1,  5,  9],
       [10, 11, 13],
       [12, 13, 15]
    ]
    k = 7

    print Solution().kthSmallest(matrix, k)
