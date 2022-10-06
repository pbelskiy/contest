class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        def solve(h, m, r):
            if sum(h) > 11 or sum(m) > 59:
                return

            if r == 0:
                times.add(f'{sum(h)}:{sum(m):02}')
                return

            for v in (8, 4, 2, 1):
                if v not in h:
                    solve(h | {v}, m, r - 1)

            for v in (32, 16, 8, 4, 2, 1):
                if v not in m:
                    solve(h, m | {v}, r - 1)

        if turnedOn > 8:
            return []

        # I am too lazy now to use bitmask :-)
        times = set()
        solve(set(), set(), turnedOn)
        return times
