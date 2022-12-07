class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        @cache
        def solve(i, r):
            if r > 0 and i == len(nums):
                return float('-inf')

            if r == 0 and i < len(nums):
                return float('-inf')

            s, m = 0, 0
            for j in range(i, len(nums)):
                s += nums[j]
                m = max(m, solve(j + 1, r - 1) + (s / (j - i + 1)))

            return m

        return solve(0, k)
