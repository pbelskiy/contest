"""
Use bisect with helper function which gives answer
is it possible to split nums into groups of numbers
where each group sum less or equal to x.

TC: O(MlgN)
SC: O(1)
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def is_possible(x):
            n = len(nums)
            t = 0
            g = 0

            for i in range(n):
                # cannot be in any group
                if nums[i] > x:
                    return False

                # add it to current group
                if t + nums[i] <= x and n - i + 1 > k - g:
                    t += nums[i]
                    continue

                # start new group
                t = nums[i]
                g += 1

            # last group
            if t <= x:
                g += 1

            return g == k

        lo, hi = 0, sum(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
