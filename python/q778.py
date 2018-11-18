import heapq


class MinHeap(object):
    def __init__(self):
        self.heap = []

    def push(self, v):
        heapq.heappush(self.heap, v)

    def pop(self):
        return heapq.heappop(self.heap)

    def getMin(self):
        if not self.heap:
            return None
        return self.heap[0]

    def getLength(self):
        return len(self.heap)


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        # elements in heap is (height, row, col)
        seen = set()
        heap = MinHeap()
        heap.push((grid[0][0], 0, 0))

        while heap.getLength():
            height, row, col = heap.pop()
            if row == N-1 and col == N-1:
                return height

            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r <= N-1 and 0 <= c <= N-1 and (r,c) not in seen:
                    h = max(height, grid[r][c])
                    heap.push((h, r, c))
                    seen.add((r,c))


if __name__ == "__main__":

    grid = [[0,2],[1,3]]
    print Solution().swimInWater(grid)