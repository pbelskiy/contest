class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        lo, hi = 1, max(candies)
        while lo <= hi:
            mid = (lo + hi) // 2
            if sum(n // mid for n in candies) >= k:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
