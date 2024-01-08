class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q = deque([(x, 0)])
        v = set()
        while q:
            x, t = q.popleft()
            if x == y:
                return t

            v.add(x)

            if x % 11 == 0 and x // 11 not in v:
                q.append((x // 11, t + 1))

            if x % 5 == 0 and x // 5 not in v:
                q.append((x // 5, t + 1))

            if x - 1 not in v:
                q.append((x - 1, t + 1))

            if x + 1 not in v:
                q.append((x + 1, t + 1))
