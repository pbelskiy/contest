class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def is_both(y, x):
            visited = set([(y, x)])
            q = deque([(y, x)])
            rpo = rao = False

            while q and not (rpo and rao):
                y, x = q.popleft()

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    # reached pacific ocean
                    if dy < 0 or dx < 0:
                        rpo = True
                        continue

                    # reached atlantic ocean
                    if dy >= h or dx >= w:
                        rao = True
                        continue

                    if heights[dy][dx] > heights[y][x]:
                        continue

                    if (dy, dx) in visited:
                        continue

                    visited.add((dy, dx))
                    q.append((dy, dx))

            return rpo and rao

        points = []
        h, w = len(heights), len(heights[0])

        for y in range(h):
            for x in range(w):
                if is_both(y, x):
                    points.append((y, x))

        return points
