class Solution:
    def maxScore(self, nums: List[int]) -> int:
        m = lcm(*nums)*gcd(*nums)

        for i in range(len(nums)):
            a = nums[:i] + nums[i+1:]
            m = max(m, lcm(*a)*gcd(*a))

        return m
