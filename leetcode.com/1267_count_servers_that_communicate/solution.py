class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        def bfs(y, x):
            count = 0
            q = collections.deque([(y, x)])

            while q:
                y, x = q.popleft()

                for cy in range(h):
                    if grid[cy][x] == 1:
                        count += 1
                        grid[cy][x] = 0
                        q.append((cy, x))

                for cx in range(w):
                    if grid[y][cx] == 1:
                        count += 1
                        grid[y][cx] = 0
                        q.append((y, cx))

            return count

        total = 0
        h, w = len(grid), len(grid[0])

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 0:
                    continue

                count = bfs(y, x)
                if count > 1:
                    total += count

        return total
