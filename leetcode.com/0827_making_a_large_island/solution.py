from collections import deque
from typing import List

import random


class Solution:
    def bfs(self, grid, groups, gid, y, x):
        breadth = 0
        visited = set()
        visited.add((y, x))

        q = deque([(y, x)])

        while q:
            y, x = q.popleft()
            breadth += 1

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)):
                if (dy, dx) in visited:
                    continue

                if dy < 0 or dx < 0 or dy >= len(grid) or dx >= len(grid[0]):
                    continue

                if grid[dy][dx] == 0:
                    continue

                visited.add((dy, dx))
                q.append((dy, dx))

        for y, x in visited:
            grid[y][x] = breadth
            groups[y][x] = gid

    def largestIsland(self, grid: List[List[int]]) -> int:
        groups = [[0]*len(grid[0]) for _ in range(len(grid))]
        gid = 1

        # mark every group
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 1:
                    self.bfs(grid, groups, gid, y, x)
                    gid += 1

        maximum = grid[0][0]

        # calc sum of near groups
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != 0:
                    continue

                total = 1
                visited = set()
                for dy, dx in ((y + 1, x), (y - 1, x), (y, x - 1), (y, x + 1)):
                    if dy < 0 or dx < 0 or dy >= len(grid) or dx >= len(grid[0]):
                        continue

                    if groups[dy][dx] in visited:
                        continue

                    total += grid[dy][dx]
                    visited.add(groups[dy][dx])

                maximum = max(maximum, total)

        return maximum


print(Solution().largestIsland([
    [1, 1],
    [1, 1]
]), 4)

print(Solution().largestIsland([
    [1, 0],
    [0, 1]
]), 3)

print(Solution().largestIsland([
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
]), 6)

grid = []
random.seed(0)

for x in range(500):
    row = []
    for y in range(500):
        row.append(random.randint(0, 1))

    grid.append(row)

print(Solution().largestIsland(grid), 647)
