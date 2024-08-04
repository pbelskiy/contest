class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.g = grid
        self.n = len(grid)
        self.d = defaultdict(list)

        for y in range(self.n):
            for x in range(self.n):
                self.d[grid[y][x]].append((y, x))

    def adjacentSum(self, value: int) -> int:
        t = 0

        for y, x in self.d[value]:
            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < self.n and 0 <= dx < self.n):
                    continue

                t += self.g[dy][dx]

        return t

    def diagonalSum(self, value: int) -> int:
        t = 0

        for y, x in self.d[value]:
            for dy, dx in ((y + 1, x - 1), (y + 1, x + 1), (y - 1, x + 1), (y - 1, x - 1)):
                if not (0 <= dy < self.n and 0 <= dx < self.n):
                    continue

                t += self.g[dy][dx]

        return t
