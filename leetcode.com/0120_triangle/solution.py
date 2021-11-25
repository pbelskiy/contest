class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for r in range(1, len(triangle)):
            w = len(triangle[r])
            for c in range(w):
                if c == 0:
                    triangle[r][c] += triangle[r - 1][c]
                elif c == w - 1:
                    triangle[r][c] += triangle[r - 1][c - 1]
                else:
                    triangle[r][c] += min(triangle[r - 1][c], triangle[r - 1][c - 1])

        return min(triangle[-1])
