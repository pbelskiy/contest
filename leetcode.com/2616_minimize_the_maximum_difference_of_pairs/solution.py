class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        def is_possible(d):
            t = 0
            i = 0

            while i < len(nums) - 1:
                if abs(nums[i] - nums[i + 1]) <= d:
                    t += 1
                    i += 2
                else:
                    i += 1

            return t >= p

        nums.sort()

        lo, hi = 0, max(nums) - min(nums)
        while lo <= hi:
            mid = (lo  + hi) // 2
            if is_possible(mid):
                hi = mid - 1
            else:
                lo = mid + 1

        return lo
