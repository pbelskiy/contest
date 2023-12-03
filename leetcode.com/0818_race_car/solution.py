class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])
        v = set()

        while q:
            p, s, t = q.popleft()
            if p == target:
                return t

            if (p + s, s*2) not in v:
                q.append((p + s, s*2, t + 1))
                v.add((p + s, s*2))

            if s > 0 and (p, -1) not in v:
                q.append((p, -1, t + 1))
                v.add((p, -1))

            if s < 0 and (p, 1) not in v:
                q.append((p, 1, t + 1))
                v.add((p, 1))
