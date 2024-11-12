"""
Greedy scan, simple math and logic.

TC: O(N)
SC: O(1)
"""
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        t = 0

        for y in range(h):
            for x in range(w):

                # bottom and top
                if grid[y][x] > 0:
                    t += 2

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):

                    # external sides adds height of block
                    if not (0 <= dy < h and 0 <= dx < w):
                        t += grid[y][x]

                    # current block not overlapped by others
                    elif grid[y][x] > grid[dy][dx]:
                        t += grid[y][x] - grid[dy][dx]

        return t
