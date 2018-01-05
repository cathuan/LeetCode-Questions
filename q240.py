class Solution(object):

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        nRows = len(matrix)
        if nRows == 0:
            return False
        nCols = len(matrix[0])
        if nCols == 0:
            return False

        for i in range(nRows):
            if self.isInRow(matrix[i], target):
                if self.searchInRow(matrix[i], target):
                    return True
        return False

    def isInRow(self, nums, target):

        return not (nums[0] > target or nums[-1] < target)

    def searchInRow(self, nums, target):

        i = 0
        j = len(nums)-1
        if nums[i] == target:
            return True
        if nums[j] == target:
            return True

        while j - i > 1:
            mid = (i+j)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                i = mid
            else:
                j = mid
        return False


if __name__ == "__main__":

    matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

    print Solution().searchMatrix(matrix, 9)
