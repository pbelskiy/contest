class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        def get_total(sy, sx):
            t = 0

            for y in range(sy, h):
                s = 0

                for x in range(sx, w):

                    if sy == y:
                        s += matrix[sy][x]
                    elif sy == 0:
                        s += ps[y][x]
                    else:
                        s += ps[y][x] - ps[sy - 1][x]

                    if s == target:
                        t += 1

            return t

        t, h, w = 0, len(matrix), len(matrix[0])

        ps = deepcopy(matrix)
        for x in range(w):
            for y in range(1, h):
                ps[y][x] += ps[y - 1][x]

        for y in range(h):
            for x in range(w):
                t += get_total(y, x)

        return t
