class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        q = deque([(start[1], start[0], 0)])
        v = set()
        while q:
            y, x, m = q.popleft()
            if m % 2 == 0 and [y, x] == target:
                return True

            if abs(y) > 7 or abs(x) > 7:
                continue

            for dy, dx in (
                (y + 1, x - 2),
                (y + 1, x + 2),
                (y + 2, x - 1),
                (y + 2, x + 1),
                (y - 1, x - 2),
                (y - 1, x + 2),
                (y - 2, x - 1),
                (y - 2, x + 1),
            ):
                if (dy, dx) not in v:
                    q.append((dy, dx, m + 1))
                    v.add((dy, dx))

        return False

