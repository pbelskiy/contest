"""
Use binary search here with helper function, which
gives us answer - is it possible to do all work with
given time limit.

TC: O(NlgM)
SC: O(1)
"""
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def is_possible(limit):
            h = mountainHeight

            for t in workerTimes:
                h -= int((-1 + math.sqrt(1 + 8 * limit / t)) // 2)
                if h <= 0:
                    return True

            return h <= 0

        lo, hi = 0, 10**24
        while lo < hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
