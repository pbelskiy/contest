"""
TC: O(NlogM)
SC: O(1)
"""
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def possible(v):
            d = 0

            for i in range(len(nums) - 1, -1, -1):
                if nums[i] + d <= v:
                    d = 0
                else:
                    d += nums[i] - v

            return d == 0

        lo, hi = 0, max(nums)

        while lo <= hi:
            mid = (lo + hi) // 2

            if possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
