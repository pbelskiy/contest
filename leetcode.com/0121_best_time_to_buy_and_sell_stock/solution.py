class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        minimum = 10**5

        for n in prices:
            minimum = min(minimum, n)

            if n > minimum:
                best = max(best, n - minimum)

        return best
