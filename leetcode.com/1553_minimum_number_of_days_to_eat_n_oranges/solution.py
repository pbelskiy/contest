class Solution:
    def minDays(self, n: int) -> int:
        q = collections.deque([(0, n)])
        v = set()

        while q:
            d, r = q.popleft()
            if r in v:
                continue

            v.add(r)
            if r == 0:
                return d

            q.append((d + 1, r - 1))

            if r % 2 == 0:
                q.append((d + 1, r - (r // 2)))

            if r % 3 == 0:
                q.append((d + 1, r - (2 * (r // 3))))
