class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:

        def is_magic(y, x):
            s = set()

            # check rows
            for d in range(3):
                row = grid[y+d][x:x+3]
                s |= set(row)
                if sum(row) != 15:
                    return False

            # check for unique
            if s != set(list(range(1, 10))):
                return False

            # check cols
            for d in range(3):
                if grid[y][x+d] + grid[y+1][x+d] + grid[y+2][x+d] != 15:
                    return False

            # check diagonal
            s = 0
            for d in range(3):
                s += grid[y+d][x+d]
            if s != 15:
                return False

            return True

        t = 0

        h, w = len(grid), len(grid[0])
        for y in range(h - 2):
            for x in range(w - 2):
                if is_magic(y, x):
                    t += 1

        return t
