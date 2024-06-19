class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def is_possible(d):
            t = 0
            f = 0

            for n in bloomDay:
                if n <= d:
                    f += 1
                else:
                    t += f // k
                    f = 0

            t += f // k
            return t >= m

        lo, hi = 1, max(bloomDay)
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        if not is_possible(lo):
            return -1

        return lo
