class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:

        def bfs(t):
            fq, fv = deque(), set()
            eq, ev = deque([(0, 0)]), set((0, 0))

            # add fire start points
            for y, x in product(range(h), range(w)):
                if grid[y][x] == 1:
                    fv.add((y, x))
                    fq.append((y, x))

            m = 0
            while fq or eq:
                # spread fire
                q = deque()
                while fq:
                    y, x = fq.popleft()
                    fv.add((y, x))

                    for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                        if not (0 <= y < h and 0 <= x < w):
                            continue

                        if grid[y][x] == 2 or (y, x) in fv:
                            continue

                        q.append((y, x))

                if not q:
                    m = t

                fq = q
                m += 1

                # try to escape
                if m >= t:
                    if not eq:
                        return False, (0, 0) in fv

                    q = deque()
                    while eq:
                        y, x = eq.popleft()
                        if y == h - 1 and x == w - 1:
                            return True, (0, 0) in fv

                        if (y, x) in fv:
                            continue

                        for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                            if not (0 <= y < h and 0 <= x < w):
                                continue

                            if grid[y][x] == 2 or (y, x) in fv or (y, x) in ev:
                                continue

                            ev.add((y, x))
                            q.append((y, x))

                    eq = q

            return False, (0, 0) in fv

        h, w = len(grid), len(grid[0])

        can_escape, _ = bfs(0)
        _, can_fire_reach_me = bfs(10**9)

        if can_escape is not True:
            return -1

        if can_fire_reach_me is not True:
            return 10**9

        lo, hi = 0, 10**4
        while lo <= hi:
            mid = (lo + hi) // 2
            can_escape, _ = bfs(mid)
            if can_escape:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi - 1
