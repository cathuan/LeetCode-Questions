# run time 3ms beats 53.88%
# memory usage 18.73MB beats 5.53% which is O(n)
from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # If we have duplicated numbers then there are two target/2 in the list.
        if target % 2 == 0 and len([num for num in nums if num == target/2]) == 2:
            answer = []
            for idx, num in enumerate(nums):
                if num != target / 2:
                    continue
                answer.append(idx)
            return answer

        # now we are sure that no numbers are duplicated
        num_to_index = self.get_num_to_index(nums)  # num -> index in the list

        for idx, num in enumerate(nums):
            if num == target / 2:
                continue
            if target - num in num_to_index:
                return sorted([idx, num_to_index[target-num]])

        raise ValueError()

    def get_num_to_index(self, nums: List[int]) -> Dict[int, int]:
        rets = {}
        for idx, num in enumerate(nums):
            rets[num] = idx
        return rets