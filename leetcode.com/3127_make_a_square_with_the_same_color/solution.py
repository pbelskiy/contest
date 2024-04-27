class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def check(y, x):
            b = w = 0

            for dy, dx in ((x, y), (x + 1, y), (x, y + 1), (x + 1, y +1)):
                if grid[dy][dx] == 'B':
                    b += 1
                else:
                    w += 1

            return b >= 3 or w >= 3

        for y in range(2):
            for x in range(2):
                if check(y, x):
                    return True

        return False
