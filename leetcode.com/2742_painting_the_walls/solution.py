"""
Сalculate the minimum cost to buy enough time to finish n walls.

TC: O(N^2)
SC: O(N^2)
"""
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @cache
        def dp(i, w):
            if w <= 0:  # all walls are painted
                return 0

            if i == n:  # no painters left
                return float('inf')

            return min(
                # go next painter and decrease walls left
                dp(i + 1, w - time[i] - 1) + cost[i],
                # or just go next painter
                dp(i + 1, w)
            )

        n = len(cost)
        return dp(0, n)  # painter index, walls left
