class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        @cache
        def dp(i, p):
            if i == len(nums):
                return p

            return max(
                dp(i + 1, p*nums[i]),  # continue product multiply
                dp(i + 1, nums[i]),    # start new product
                p,                     # or just current product
            )

        return dp(1, nums[0])
