from typing import List
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(heap, (num, idx))
        
        mark = 0
        seen_idx = set()
        while len(heap) > 0:
            num, idx = heapq.heappop(heap)
            if idx not in seen_idx:
                mark += num
                seen_idx.add(idx)
                if idx - 1 >= 0:
                    seen_idx.add(idx-1)
                if idx + 1 < len(nums):
                    seen_idx.add(idx+1)
        return mark


if __name__ == "__main__":
    nums = [2, 3, 5, 1, 3, 2]
    print(Solution().findScore(nums))
            