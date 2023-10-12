class Solution:

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        # find peak
        lo, hi = 0, length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            peak = mountain_arr.get(mid)

            left = mountain_arr.get(mid - 1) if mid - 1 >= 0 else peak + 1
            if left > peak:
                hi = mid - 1
                continue

            right = mountain_arr.get(mid + 1) if mid + 1 <= length - 1 else peak + 1
            if right > peak:
                lo = mid + 1
                continue

            break

        peak_index = mid
        if peak == target:
            return peak_index

        # find target on left side from peak
        lo, hi = 0, peak_index - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            elif v < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # find target on right side from peak
        lo, hi = peak_index + 1, length - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = mountain_arr.get(mid)
            if v == target:
                return mid
            elif v > target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1
