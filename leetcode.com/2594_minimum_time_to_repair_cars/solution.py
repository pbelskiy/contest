class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def possible(m):
            rest = cars

            for r in ranks:
                rest -= int(math.sqrt(m // r))

            return rest <= 0

        lo, hi = 1, 10**14
        while lo <= hi:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
