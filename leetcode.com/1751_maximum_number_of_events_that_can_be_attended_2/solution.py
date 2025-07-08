class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        @cache
        def dfs(i, k):
            if k == 0 or i >= len(events):
                return 0

            j = bisect.bisect_left(events, events[i][1] + 1, key=lambda t: t[0])

            # take
            m = dfs(j, k - 1) + events[i][2]

            # skip
            return max(m, dfs(i + 1, k))

        events.sort()
        return max(dfs(i, k) for i in range(len(events)))

