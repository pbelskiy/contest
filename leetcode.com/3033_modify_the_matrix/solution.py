class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rev = list(zip(*matrix))

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] != -1:
                    continue

                matrix[y][x] = max(rev[x])

        return matrix
