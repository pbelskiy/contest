class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        for n in range(1, numRows):
            row = []
            size = len(triangle[-1]) + 1

            for i in range(size):
                if i == 0 or i == size - 1:
                    row.append(1)
                else:
                    row.append(triangle[-1][i-1] + triangle[-1][i])

            triangle.append(row)

        return triangle
