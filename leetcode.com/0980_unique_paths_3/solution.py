class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def dfs(y, x, v):
            nonlocal total

            if grid[y][x] == 2:
                if len(v) == empties:
                    total += 1
                    # print(list(sorted(v)))

                return

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if grid[cy][cx] == -1:
                    continue

                if (cy, cx) in v:
                    continue

                cv = copy.deepcopy(v)
                cv.add((cy, cx))
                dfs(cy, cx, cv)

        h, w = len(grid), len(grid[0])
        total, empties, obstacles = 0, 0, 0

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    start = (y, x)
                elif grid[y][x] == -1:
                    obstacles += 1

        empties = h*w - obstacles
        y, x = start
        v = {(y, x)}
        # print(v)
        dfs(y, x, v)
        return total
