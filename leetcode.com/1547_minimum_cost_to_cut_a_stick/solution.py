class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        @cache
        def dp(left, right):
            cost = right - left
            m = float('inf')

            for mid in cuts:
                if left < mid < right:
                    m = min(m, dp(left, mid) + dp(mid, right) + cost)

            if m == float('inf'):
                return 0

            return m

        return dp(0, n)
