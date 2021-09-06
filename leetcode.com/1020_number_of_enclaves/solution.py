class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        visited = set()

        def bfs(y, x):
            if grid[y][x] == 0:
                return

            q = collections.deque()
            q.append((y, x))
            visited.add((y, x))

            while q:
                cy, cx = q.popleft()

                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ny = cy + dy
                    nx = cx + dx

                    if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited:
                        if grid[ny][nx] == 1:
                            visited.add((ny, nx))
                            q.append((ny, nx))

        # walk by edges
        for dy in range(n):
            bfs(dy, 0)
            bfs(dy, m - 1)

        for dx in range(m):
            bfs(0, dx)
            bfs(n - 1, dx)

        # calc not visited
        count = 0
        for y in range(n):
            for x in range(m):
                if grid[y][x] == 1 and (y, x) not in visited:
                    count += 1
                    continue

        return count
