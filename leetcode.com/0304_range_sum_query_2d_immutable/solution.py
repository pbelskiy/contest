class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []

        for row in matrix:
            p, s = [], 0

            for v in row:
                s += v
                p.append(s)

            self.prefix.append(p)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0

        for r in range(row1, row2 + 1):
            s += self.prefix[r][col2]

            if col1 > 0:
                s -= self.prefix[r][col1 - 1]

        return s
