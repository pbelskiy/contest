class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def get_pairs_count_lt(x):
            t = 0

            for i in range(len(nums)):
                j = bisect.bisect(nums, nums[i] + x)
                t += j - i - 1

            return t

        nums.sort()

        lo, hi = 0, max(nums)

        while lo <= hi:
            mid = (lo + hi) // 2
            if get_pairs_count_lt(mid) < k:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo
