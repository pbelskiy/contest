"""
Use binary search here. Write funciton `check` which return true or
false if Koko could eat bananas with speed `s`.

Then using binary search approach use that function to find minimal
speed.

TC: O(NlogM)
SC: O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(s):
            r, i = h, 0

            while r > 0 and i < len(piles):
                r -= math.ceil(piles[i] / s)
                i += 1

            return r >= 0 and i == len(piles)

        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
