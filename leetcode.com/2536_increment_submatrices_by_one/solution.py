class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        m = [[0]*n for _ in range(n)]

        # add markers
        for y1, x1, y2, x2 in queries:
            for y in range(y1, y2 + 1):
                m[y][x1] += 1
                if x2 + 1 < n:
                    m[y][x2 + 1] -= 1

        # real apply operations
        for y in range(n):
            v = 0
            for x in range(n):
                v += m[y][x]
                m[y][x] = v

        return m

