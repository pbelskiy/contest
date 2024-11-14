class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def is_possible(x):
            t = 0

            for q in quantities:
                t += math.ceil(q / x)

            return n >= t

        lo, hi = 1, max(quantities)
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
