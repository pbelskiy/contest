class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        h, w = len(matrix), len(matrix[0])

        matrix = list(map(list, zip(*matrix)))
        for row in matrix:
            for i in range(1, len(row)):
                if row[i] > 0:
                    row[i] += row[i - 1]

        matrix.sort()
        matrix = list(map(list, zip(*matrix)))
        # for row in matrix:
        #     print(row)
        # return 0

        best = 0

        for y in range(h):
            matrix[y].sort()
            for x in range(w - 1, -1, -1):
                height = matrix[y][x]
                width = w - x
                # print(f'y={y}, x={x}, height={height}, width={width} => A={height * width}')
                best = max(best, height * width)

        return best
