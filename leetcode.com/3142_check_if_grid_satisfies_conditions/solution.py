class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        h, w = len(grid), len(grid[0])

        # check right
        for y in range(h):
            for x in range(w - 1):
                if grid[y][x] == grid[y][x + 1]:
                    return False

        # check up
        for x in range(w):
            if len(set(grid[y][x] for y in range(h))) != 1:
                return False

        return True
