class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        v = set(q)
        m = s

        while q:
            s = q.popleft()
            m = min(m, s)

            # add
            ss = list(map(int, s))
            for i in range(1, len(ss), 2):
                ss[i] = (ss[i] + a) % 10
            ss = ''.join(map(str, ss))

            if ss not in v:
                v.add(ss)
                q.append(ss)

            # rotate
            ss = s[b:] + s[:b]
            if ss not in v:
                v.add(ss)
                q.append(ss)

        return m

