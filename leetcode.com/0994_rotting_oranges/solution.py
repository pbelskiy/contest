class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        sy, sx = None, None
        time, fresh = 0, 0
        q = collections.deque()

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    fresh += 1
                elif grid[y][x] == 2:
                    q.append((y, x))

        while q:
            nq = collections.deque()

            while q:
                y, x = q.popleft()

                for cy, cx in ((y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)):

                    if 0 <= cy < h and 0 <= cx < w and grid[cy][cx] == 1:
                        grid[cy][cx] = 2
                        nq.append((cy, cx))
                        fresh -= 1

            if nq:
                time += 1

            q = nq

        return -1 if fresh > 0 else time
