"""
Simple idea with binary search.

Write function which checks possibility to send all weights
with limit of ship `w`. It linear check which took O(N) time
complexity.

Then using this function we write binary search to find minimal
possible capacity. Final time complxity is O(N) * O(logN) = O(NlogN)

TC: O(NlogN)
SC: O(1)
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(w):
            d = days
            i = 0

            while d > 0:
                s = 0
                while i < len(weights) and s + weights[i] < w:
                    s += weights[i]
                    i += 1

                if s == 0:
                    break

                d -= 1

            return i == len(weights)

        lo, hi = 1, sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return hi
