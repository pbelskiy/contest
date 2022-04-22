class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:

        def reverse_diagonal(y1, x1):
            y2 = len(matrix) - 1 - x1
            x2 = len(matrix) - 1 - y1

            while y1 < y2:
                matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]
                y1, x1 = y1 + 1, x1 + 1
                y2, x2 = y2 - 1, x2 - 1

        def rotate():
            for row in matrix:
                row.reverse()

            # reverse left-right diagonals
            for i in range(len(matrix[0]) - 2, -1, -1):
                reverse_diagonal(0, i)

            for i in range(1, len(matrix)):
                reverse_diagonal(i, 0)

        for _ in range(4):
            if matrix == target:
                return True

            rotate()

        return False
