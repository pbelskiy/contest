class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        def get_ranks():
            ranks = {}

            q = deque()
            for y, x in product(range(h), range(w)):
                if grid[y][x] == 1:
                    q.append((y, x, y, x))
                    ranks[(y, x)] = 0

            while q:
                y, x, ty, tx = q.popleft()

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if (dy, dx) in ranks:
                        continue

                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    ranks[(dy, dx)] = abs(dy - ty) + abs(dx - tx)
                    q.append((dy, dx, ty, tx))

            return ranks

        def get_max_factor(ranks):
            q = [(-ranks[(0, 0)], 0, 0)]
            v = set([(0, 0)])

            while q:
                m, y, x = heappop(q)
                if y == h - 1 and x == w - 1:
                    return -m

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if (dy, dx) in v:
                        continue

                    if not (0 <= dy < h and 0 <= dx < w):
                        continue

                    v.add((dy, dx))
                    heappush(q, (-min(-m, ranks[(dy, dx)]), dy, dx))

            return -1

        h, w = len(grid), len(grid[0])
        ranks = get_ranks()
        return get_max_factor(ranks)
