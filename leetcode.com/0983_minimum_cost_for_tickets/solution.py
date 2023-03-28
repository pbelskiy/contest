"""
Here we use simple approach of dynamic programimng.
Initially just write recursion, then add @cache decorator.

TC: O(N)
SC: O(N)
"""
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def solve(i):
            if i >= len(days):
                return 0

            m = float('inf')
            for d, c in zip((1, 7, 30), costs):
                m = min(m, solve(bisect.bisect_left(days, days[i] + d)) + c)

            return m

        return solve(0)
