from typing import List
import bisect


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Longest increasing sequence
        lis = self.calculate_lis(nums)
        # Longest decreasing sequence
        lds = self.calculate_lis(nums[::-1])[::-1]

        max_length = 0
        for idx in range(len(nums)):
            if lis[idx] > 1 and lds[idx] > 1:
                max_length = max(max_length, lis[idx] + lds[idx]-1)
        return len(nums) - max_length

    def calculate_lis(self, v: List[int]) -> List[int]:
        lis_len = [1] * len(v)
        lis = [v[0]]

        for i in range(1, len(v)):
            index = bisect.bisect_left(lis, v[i])

            # Add to the list if v[i] is greater than the last element
            if index == len(lis):
                lis.append(v[i])
            else:
                # Replace the element at index with v[i]
                # This is useful but won't make lis a real lis -- only equivalent lis.
                # For example, nums=[6, 7, 1, 2, 3]. Then at idx=1 we have lis=[6, 7]
                # Next go to i=2, we have lis [1, 7], and then [1, 2], and then [1, 2, 3]. So this allow us to eventually go to 3.
                lis[index] = v[i]

            lis_len[i] = len(lis)

        return lis_len