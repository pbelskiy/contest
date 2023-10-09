class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        for y in range(1, len(matrix)):
            for x in range(1, len(matrix[0])):
                if matrix[y][x] == 0:
                    continue

                matrix[y][x] = min(
                    matrix[y - 1][x],
                    matrix[y - 1][x - 1],
                    matrix[y][x - 1]
                ) + 1

        return sum(sum(row) for row in matrix)
