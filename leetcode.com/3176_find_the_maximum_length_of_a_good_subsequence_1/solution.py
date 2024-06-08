class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:

        @cache
        def dp(i, k):
            m = 0

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    m = max(m, dp(j, k) + 1)
                elif k > 0:
                    m = max(m, dp(j, k - 1) + 1)

            return m

        return max(dp(i, k) + 1 for i in range(len(nums)))
