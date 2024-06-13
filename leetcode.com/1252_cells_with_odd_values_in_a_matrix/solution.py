class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0]*n for _ in range(m)]

        for y, x in indices:
            for dx in range(n):
                matrix[y][dx] += 1

            for dy in range(m):
                matrix[dy][x] += 1

        t = 0
        for row in matrix:
            for n in row:
                t += n % 2

        return t
