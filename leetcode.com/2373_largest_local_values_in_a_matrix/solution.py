class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n1 = len(grid)
        n2 = n1 - 2

        mat = [[0]*n2 for _ in range(n2)]

        for y in range(1, n1 - 1):
            for x in range(1, n1 - 1):
                v = 0

                for dy, dx in (
                    (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                    (y, x - 1), (y, x), (y, x + 1),
                    (y + 1, x - 1), (y + 1, x), (y + 1, x + 1),
                ):
                    v = max(v, grid[dy][dx])

                mat[y - 1][x - 1] = v

        return mat
