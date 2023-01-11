class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()

        s, p = 0, [0]
        for n in arr:
            s += n
            p.append(s)

        # get sum using prefix sum above
        def get(v):
            i = bisect.bisect_left(arr, v)
            a = p[i]
            b = v*(len(arr) - i)
            return a + b

        diff = float('inf')
        value = float('inf')

        lo, hi = 0, arr[-1] + 1

        # binary search
        while lo < hi:
            mid = (lo + hi) // 2
            s = get(mid)
            d = abs(target - s)

            if d < diff or (d == diff and mid < value):
                diff = d
                value = mid

            if s == target:
                return mid
            elif s < target:
                lo = mid + 1
            else:
                hi = mid

        return value
