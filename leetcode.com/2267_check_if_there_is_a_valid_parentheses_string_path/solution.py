class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:

        @cache
        def dp(y, x, b):
            if grid[y][x] == '(':
                b += 1
            else:
                b -= 1

            if b < 0:
                return False

            if y == h - 1 and x == w - 1 and b == 0:
                return True

            if y + 1 < h and dp(y + 1, x, b):
                return True

            if x + 1 < w and dp(y, x + 1, b):
                return True

            return False

        h, w = len(grid), len(grid[0])
        return dp(0, 0, 0)
