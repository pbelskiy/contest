"""
Sliding window.

TC: O(N)
SC: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # profit without modification
        best = t = sum(p * s for p, s in zip(prices, strategy))

        # update initial chunk
        for i in range(k):
            t -= prices[i] * strategy[i]
        for i in range(k // 2, k):
            t += prices[i] * 1

        best = max(best, t)

        # sliding window
        mid = k // 2
        left = 0
        for right in range(k, len(prices)):
            # revert left
            t += prices[left] * strategy[left]
            # update mid (hold)
            t -= prices[mid] * 1
            # update right (sell)
            t -= prices[right] * strategy[right]
            t += prices[right] * 1

            left += 1
            mid += 1
            best = max(best, t)

        return best

