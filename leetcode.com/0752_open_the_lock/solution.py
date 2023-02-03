class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([('0000', 0)])
        v = set(['0000'])
        d = set(deadends)

        while q:
            s, m = q.popleft()
            if s in d:
                continue

            if s == target:
                return m

            for i in range(4):
                for val in ((int(s[i]) - 1) % 10, (int(s[i]) + 1) % 10):
                    ns = s[:i] + str(val) + s[i+1:]
                    if ns not in v:
                        v.add(ns)
                        q.append((ns, m + 1))

        return -1
