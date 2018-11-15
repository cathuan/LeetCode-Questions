class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        opponents = {}
        for index, value in enumerate(nums):
            opponent = target - value
            if opponent in opponents:
                return [opponents[opponent], index]

            opponents[value] = index

        # based on the assumption of the question, we will never achieve here.
        assert False


if __name__ == "__main__":

    solution = Solution()
    s = solution.twoSum([3, 2, 4], 6)
    print(s)
