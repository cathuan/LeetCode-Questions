from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        buildings = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    buildings += 1
        
        hit = [[0] * n for _ in range(m)]
        dists = [[0] * n for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    if not self.BFS(row, col, buildings, grid, hit, dists):
                        return -1
        
        minDist = float("inf")
        seen = False
        for row in range(m):
            for col in range(n):
                if hit[row][col] != buildings:
                    continue
                if grid[row][col] != 0:
                    continue
                minDist = min(minDist, dists[row][col])
                seen = True
        if not seen:
            minDist = -1
        return minDist

    def BFS(self, row, col, buildings, grid, hit, dists):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[row][col] = True
        count1 = 1
        queue = deque()
        queue.append((row, col, 0))

        while queue:
            x, y, dist = queue.popleft()
            for i, j in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                    continue
                visited[i][j] = True
                if grid[i][j] == 0:
                    queue.append((i, j, dist+1))
                    hit[i][j] += 1
                    dists[i][j] += dist + 1
                elif grid[i][j] == 1:
                    count1 += 1
        return count1 == buildings
