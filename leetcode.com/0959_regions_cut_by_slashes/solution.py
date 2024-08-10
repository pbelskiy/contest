"""
Transform grid to more convinient form and use BFS.

We have two forms '\' and '/'.

Let '\' be:
    [1 0 0]
    [0 1 0]
    [0 0 1]

And '/' be:
    [0 0 1]
    [0 1 0]
    [1 0 0]

Then we can use simple BFS here after grid transformation.

TC: O(N)
SC: O(N)
"""

class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        m = [[0]*n*3 for _ in range(n*3)]

        # transform to convinient matrix
        for y in range(n):
            for x in range(n):
                if grid[y][x] == '/':
                    m[y*3][x*3 + 2] = 1
                    m[y*3 + 1][x*3 + 1] = 1
                    m[y*3 + 2][x*3] = 1
                elif grid[y][x] == '\\':
                    m[y*3][x*3] = 1
                    m[y*3 + 1][x*3 + 1] = 1
                    m[y*3 + 2][x*3 + 2] = 1

        def bfs(y, x):
            q = deque([(y, x)])

            while q:
                y, x = q.popleft()

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= dy < n and 0 <= dx < n):
                        continue

                    if m[dy][dx] == 1:
                        continue

                    m[dy][dx] = 1
                    q.append((dy, dx))

        n = len(m)
        t = 0

        for y in range(n):
            for x in range(n):
                if m[y][x] == 0:
                    t += 1
                    bfs(y, x)

        return t
