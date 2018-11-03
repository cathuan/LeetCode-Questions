import heapq


class Solution(object):

    def mincostToHireWorkers(self, quality, wage, K):

        workers = sorted((w*1.0/q, q, w) for q, w in zip(quality, wage))

        ans = float("inf")
        heap = []  # maximum heap, storing -q since heapq generates a min heap.
        total_q = 0

        for r, q, w in workers:
            heapq.heappush(heap, -q)
            total_q += q

            if len(heap) > K:
                max_q = -heapq.heappop(heap)
                total_q -= max_q

            if len(heap) == K:
                ans = min(ans, total_q * r)

        return ans
