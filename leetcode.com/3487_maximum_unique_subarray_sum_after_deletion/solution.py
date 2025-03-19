class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m = max(nums)
        s = set([n for n in nums if n > 0])
        if s:
            return max(m, sum(s))
        return m
