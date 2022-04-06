class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        return int(math.sqrt(x))

   def mySqrt2(self, x: int) -> int:
        if x == 1:
            return 1

        lo, hi = 0, x // 2

        while lo <= hi:
            mid = (lo + hi) // 2

            s = mid * mid

            if s == x:
                return mid

            if s < x:
                lo = mid + 1
            else:
                hi = mid - 1

        return hi
