from typing import List
import bisect


# Binary search
class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        # Sort value of nums
        nums.sort()

        # For each num, find num+2k
        max_beauty = 0
        for i, num in enumerate(nums):
            # So j == len(nums) if num + 2k >= all nums, or nums[j] >= num + 2k
            j = bisect.bisect(nums, num + 2*k)
            length = j-i
            max_beauty = max(max_beauty, length)
        return max_beauty


if __name__ == "__main__":

    nums = [1, 1, 1, 1]
    k = 2
    print(Solution().maximumBeauty(nums, k))