class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def get(n):
            s = 0
            for t in time:
                s += n // t

            return s

        lo, hi = 1, min(time)*totalTrips
        while lo <= hi:
            mid = (lo + hi) // 2
            if get(mid) < totalTrips:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo
