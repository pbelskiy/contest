class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def bfs(i):
            v = set(tuple(cells[j]) for j in range(i))
            q = deque()

            for x in range(1, col + 1):
                if (1, x) not in v:
                    q.append((1, x))

            while q:
                y, x = q.popleft()
                if y == row:
                    return True

                for y, x in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (1 <= y <= row and 1 <= x <= col):
                        continue

                    if (y, x) in v:
                        continue

                    q.append((y, x))
                    v.add((y, x))

            return False

        lo, hi = 0, len(cells)
        while lo <= hi:
            mid = (lo + hi) // 2
            if bfs(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
