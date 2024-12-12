from typing import List
from heapq import heappush, heappop
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heappush(heap, -gift)

        for idx in range(k):
            gift = - heappop(heap)
            if gift == 1:
                return len(gifts)
            new_gift = int(math.sqrt(gift))
            heappush(heap, -new_gift)

        return -sum(heap)