class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        def is_valid(left, right):
            for arr in nums:
                a = bisect.bisect_left(arr, left)
                b = bisect.bisect_left(arr, right)

                if a == b == len(arr) and arr[a - 1] not in (left, right):
                    return False

                if a == b and arr[a] not in (left, right):
                    return False

            return True

        # get left and right edges
        left_min, right_max = float('inf'), float('-inf')
        for arr in nums:
            left_min, right_max = min(left_min, min(arr)), max(right_max, max(arr))

        res = [left_min, right_max]
        left = right = left_min
        best = float('inf')

        # sliding window
        prev = None
        while True:
            # extend window to right till valid using bisect
            lo, hi = left, right_max
            while lo <= hi:
                mid = (lo + hi) // 2
                if is_valid(left, mid):
                    hi = mid - 1
                else:
                    lo = mid + 1
            right = lo

            # reduce left of window till valid using bisect
            lo, hi = left, right
            while lo <= hi:
                mid = (lo + hi) // 2
                if not is_valid(mid, right):
                    hi = mid - 1
                else:
                    lo = mid + 1
            left = lo

            # write best range
            if right - left < best:
                best = right - left
                res = [left - 1, right]

            if (left, right) == prev:
                break
            prev = (left, right)

        return res
