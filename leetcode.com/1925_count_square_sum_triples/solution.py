class Solution:
    def countTriples(self, n: int) -> int:

        @cache
        def get(s):
            t = 0
            for c in range(1, n + 1):
                if s == c**2:
                    t += 1
            return t

        t = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                s = a**2 + b**2
                t += get(s)

        return t
