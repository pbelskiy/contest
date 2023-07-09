class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:

        @cache
        def dp(i):
            if i == len(nums) - 1:
                return 0

            m = 0
            for j in range(i + 1, len(nums)):
                if -target <= nums[j] - nums[i] <= target:
                    m = max(m, dp(j) + 1)

            if m == 0:
                return float('-inf')

            return m

        res = dp(0)
        if res == float('-inf'):
            return -1
        return res
