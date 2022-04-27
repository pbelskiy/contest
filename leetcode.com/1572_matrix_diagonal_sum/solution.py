class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        y, x = 0, 0
        while y < n and x < n:
            total += mat[y][x]
            x += 1
            y += 1

        y, x = n - 1, 0
        while y >= 0 and x < n:
            total += mat[y][x]
            x += 1
            y -= 1

        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total
