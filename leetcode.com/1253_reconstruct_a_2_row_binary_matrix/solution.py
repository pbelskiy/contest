class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []

        matrix = [[0]*len(colsum) for _ in range(2)]

        for i in range(len(colsum)):
            if colsum[i] == 1:
                if upper > lower:
                    matrix[0][i] = 1
                    upper -= 1
                else:
                    matrix[1][i] = 1
                    lower -= 1
            elif colsum[i] == 2:
                matrix[0][i] = 1
                matrix[1][i] = 1
                upper -= 1
                lower -= 1

            # return empty matrix
            if lower < 0 or upper < 0:
                return []

        return matrix
