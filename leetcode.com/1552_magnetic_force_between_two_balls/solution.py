class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def is_possible(f):
            last = position[0]
            rest = m - 1

            for p in position:
                if p - last < f:
                    continue

                last = p
                rest -= 1
                if rest == 0:
                    break

            return rest == 0

        position.sort()

        lo, hi = 1, position[-1]
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                lo = mid + 1
            else:
                hi = mid - 1

        return lo - 1
