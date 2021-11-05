class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        @functools.cache
        def dfs(y, x):
            best = 1

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if matrix[cy][cx] <= matrix[y][x]:
                    continue

                best = max(best, 1 + dfs(cy, cx))

            return best

        best = 0
        h, w = len(matrix), len(matrix[0])

        for y in range(h):
            for x in range(w):
                best = max(best, dfs(y, x))

        return best
