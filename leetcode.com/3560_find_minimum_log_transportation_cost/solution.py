class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0

        c1, c2 = float('inf'), float('inf')

        if n > k:
            c1 = (n - k) * k

        if m > k:
            c2 = (m - k) * k

        return min(c1, c2)

