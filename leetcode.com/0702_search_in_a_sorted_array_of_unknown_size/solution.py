class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        lo, hi = 0, 10**4
        while lo <= hi:
            mid = (lo + hi) // 2

            n = reader.get(mid)
            if n == 2**31 - 1:
                hi = mid - 1
            elif n > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return lo - 1 if reader.get(lo - 1) == target else -1
