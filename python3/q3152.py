# Runtime: 68ms, beats 35.65%
# Memory: 46.66MB, beats 42.51%
from typing import List
import bisect


class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        # Go through nums and record all numbers x, such that nums[x] and nums[x+1] are the same parity.
        same_parity_index = []
        for idx in range(len(nums) - 1):
            if nums[idx] % 2 == nums[idx+1] % 2:
                same_parity_index.append(idx)
        
        # For each pair (from, to), we need to figure out that if we can find any number x in same_parity_index,
        # such that from <= x < to.
        # bisect.bisect_left(values, i) returns idx such that values[idx] >= i and values[idx-1] < i (if idx or idx-1 exists)
        result = []
        for from_idx, to_idx in queries:
            idx = bisect.bisect_left(same_parity_index, from_idx)

            if idx == len(same_parity_index):
                result.append(True)
            else:
                value = same_parity_index[idx]
                if value < to_idx:
                    result.append(False)
                else:
                    result.append(True)
        return result
            

if __name__ == "__main__":

    # nums = [3,4,1,2,6]
    # queries = [[0, 4]]
    nums = [4,3,1,6]
    queries = [[0, 2], [2, 3]]
    result = Solution().isArraySpecial(nums, queries)
    print(result)
    import pdb; pdb.set_trace()