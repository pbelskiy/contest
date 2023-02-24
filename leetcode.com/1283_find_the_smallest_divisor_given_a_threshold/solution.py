class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if sum(math.ceil(n / mid) for n in nums) > threshold:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo
