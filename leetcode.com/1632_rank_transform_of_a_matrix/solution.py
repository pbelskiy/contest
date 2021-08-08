from typing import List
from collections import deque


#####
##### TIME LIMIT! JUST A DRAFT
#####


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        sss = set([matrix[r][c] for r in range(m) for c in range(n)])
        print(sss, len(sss))

        answer = [[1]*n for _ in range(m)]

        rows = [
            [i for i in sorted(enumerate(row), key=lambda x: x[1])] for row in matrix
        ]

        cols = []

        for c in range(n):
            col = [matrix[r][c] for r in range(m)]
            cols.append([i for i in sorted(enumerate(col), key=lambda x: x[1])])

        ###
        changed = True
        while changed:
            changed = False

            # horizontal
            for r in range(m):
                for (c1, v1), (c2, v2) in zip(rows[r], rows[r][1:]):

                    if v1 > v2 and answer[r][c1] <= answer[r][c2]:
                        answer[r][c1] += 1
                        changed = True

                    elif v1 < v2 and answer[r][c1] >= answer[r][c2]:
                        answer[r][c2] += 1
                        changed = True

                    elif v1 == v2 and answer[r][c1] != answer[r][c2]:
                        if answer[r][c1] > answer[r][c2]:
                            answer[r][c2] = answer[r][c1]
                            changed = True
                        else:
                            answer[r][c1] = answer[r][c2]
                            changed = True

            # vertical
            for c in range(n):
                for (r1, v1), (r2, v2) in zip(cols[c], cols[c][1:]):

                    if v1 > v2 and answer[r1][c] <= answer[r2][c]:
                        answer[r1][c] += 1
                        changed = True

                    elif v1 < v2 and answer[r1][c] >= answer[r2][c]:
                        answer[r2][c] += 1
                        changed = True

                    elif v1 == v2 and answer[r1][c] != answer[r2][c]:
                        if answer[r1][c] > answer[r2][c]:
                            answer[r2][c] = answer[r1][c]
                            changed = True
                        else:
                            answer[r1][c] = answer[r2][c]
                            changed = True

        return answer


a = Solution().matrixRankTransform([
    [20, -21, 14],
    [-19, 4, 19],
    [22, -47, 24],
    [-19, 4, 19]
])

for r in a:
    print(r)

# import random
# random.seed(0)
# s = 150
# m = [[random.randint(-10**9, 10**9) for _ in range(s)] for _ in range(s)]
# a = Solution().matrixRankTransform(m)
