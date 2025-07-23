class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def remove(s, p, v):
            t = 0
            q = []
            for ch in s:
                if q and q[-1] == p[0] and ch == p[1]:
                    q.pop()
                    t += v
                else:
                    q.append(ch)

            return ''.join(q), t

        t = 0

        if x > y:
            s, p = remove(s, 'ab', x)
            t += p
            s, p = remove(s, 'ba', y)
            t += p
        else:
            s, p = remove(s, 'ba', y)
            t += p
            s, p = remove(s, 'ab', x)
            t += p

        return t

