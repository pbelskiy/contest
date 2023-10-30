class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        r = 0
        t = 0

        for n in nums:
            if n == m:
                t += 1
            else:
                r = max(r, t)
                t = 0

        return max(t, r)
