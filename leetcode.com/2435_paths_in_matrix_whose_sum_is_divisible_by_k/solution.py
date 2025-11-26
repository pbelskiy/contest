"""
No need to accumulate total sum, only need to save 
mod to check divisible by k.

H = height, W = width, M = mod

TC: O(H*W*M)
SC: O(H*W*M)
"""
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        @cache
        def dfs(y, x, m):
            if y == h - 1 and x == w - 1:
                return int(m % k == 0)

            t = 0
            
            if y + 1 < h:
                t += dfs(y + 1, x, (m + grid[y + 1][x]) % k)

            if x + 1 < w:
                t += dfs(y, x + 1, (m + grid[y][x + 1]) % k)

            return t % (10**9 + 7)

        h, w = len(grid), len(grid[0])
        r = dfs(0, 0, grid[0][0])
        dfs.cache_clear()
        return r

