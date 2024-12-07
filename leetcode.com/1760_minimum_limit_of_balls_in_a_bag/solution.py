"""
Binary search on possible result.

TC: O(NlgN)
SC: O(1)
"""
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def is_possible(x):
            t = maxOperations

            for n in nums:
                t -= math.ceil((n - x) / x)

            return t >= 0

        lo, hi = 1, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
