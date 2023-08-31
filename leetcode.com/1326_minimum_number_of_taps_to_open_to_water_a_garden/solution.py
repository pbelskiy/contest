class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        d = sorted(
            [(max(0, i - r), i + r) for i, r in enumerate(ranges)],
            key=lambda t: (t[0], -t[1])
        )

        @cache
        def dfs(i, p):
            if p >= n:
                return 0

            m = float('inf')
            for j in range(i, len(d)):
                start, length = d[j]

                if start > p:
                    break

                m = min(m, dfs(j + 1, length) + 1)

            return m

        r = dfs(0, 0)
        if r == float('inf'):
            return -1

        return r
