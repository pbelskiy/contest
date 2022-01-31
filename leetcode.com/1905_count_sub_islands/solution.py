class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def bfs(y, x):
            res = True
            q = collections.deque([(y, x)])

            while q:
                cy, cx = q.popleft()

                if grid1[cy][cx] == 0:
                    res = False

                for dy, dx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    if grid2[dy][dx] == 0:
                        continue

                    grid2[dy][dx] = 0
                    q.append((dy, dx))

            return res

        total = 0
        h, w = len(grid1), len(grid1[0])

        for y in range(h):
            for x in range(w):
                if grid2[y][x] == 1 and bfs(y, x):
                    total += 1

        return total
