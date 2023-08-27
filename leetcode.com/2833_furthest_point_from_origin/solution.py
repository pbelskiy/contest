class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        @cache
        def solve(i, d):
            if i == len(moves):
                return abs(d)

            m = 0
            if moves[i] in ('L', '_'):
                m = max(m, solve(i + 1, d - 1))

            if moves[i] in ('R', '_'):
                m = max(m, solve(i + 1, d + 1))

            return m

        return solve(0, 0)
