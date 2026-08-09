class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        m = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                s = (nums[i] * nums[j]) / gcd(nums[i], nums[j])**2
                m = max(m, int(s))

        return m

