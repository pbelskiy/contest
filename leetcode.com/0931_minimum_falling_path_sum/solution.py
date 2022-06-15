class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        for y in range(1, n):
            for x in range(n):
                matrix[y][x] += min(
                    matrix[y - 1][x - 1] if x > 0 else float('inf'),
                    matrix[y - 1][x],
                    matrix[y - 1][x + 1] if x + 1 < n else float('inf'),
                )

        return min(matrix[-1])
