class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def poss(s):
            r = 0
            for i in range(len(dist) - 1):
                r += math.ceil(dist[i] / s)

            return (r + dist[len(dist) - 1] / s) <= hour

        lo, hi = 1, 10**7
        while lo <= hi:
            mid = (lo + hi) // 2
            if poss(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return -1 if lo == 10000001 else lo
