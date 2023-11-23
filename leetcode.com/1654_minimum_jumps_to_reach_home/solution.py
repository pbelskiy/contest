class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        f = set(forbidden)
        q = deque([(0, 0, 0)])
        v = set([0])

        while q:
            i, j, t = q.popleft()
            if i == x:
                return t

            if (i + a < 100000) and (i + a not in f) and ((i + a, 0) not in v):
                q.append((i + a, 0, t + 1))
                v.add((i + a, 0))

            if (i - b >= 0) and (j == 0) and ((i - b) not in f) and ((i - b, 1) not in v):
                q.append((i - b, 1, t + 1))
                v.add((i - b, 1))

        return -1
