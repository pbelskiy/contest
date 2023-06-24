class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:

        @cache
        def solve(s, aa, bb, ab):
            m = 0

            if s in ('', 'AA') and bb > 0:
                m = max(m, solve('BB', aa, bb - 1, ab) + 2)

            if s in ('', 'BB', 'AB') and aa > 0:
                m = max(m, solve('AA', aa - 1, bb, ab) + 2)

            if s in ('', 'BB', 'AB') and ab > 0:
                m = max(m, solve('AB', aa, bb, ab - 1) + 2)

            return m

        return solve('', x, y, z)
