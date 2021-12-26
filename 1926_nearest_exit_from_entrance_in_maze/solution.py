class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        h, w = len(maze), len(maze[0])
        q = collections.deque([tuple([*entrance, 0])])
        visited = set(tuple(entrance))

        while q:
            y, x, d = q.popleft()

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    # not near entrance
                    for dy, dx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                        if (dy, dx) == tuple(entrance):
                            break
                    else:
                        return d

                    continue

                if (cy, cx) in visited:
                    continue

                if maze[cy][cx] == '+':
                    continue

                q.append((cy, cx, d + 1))
                visited.add((cy, cx))

        return -1
