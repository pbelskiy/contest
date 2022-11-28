class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        @cache
        def dfs(i, n, d):
            if i == len(nums):
                return 0

            t = 0

            if n is None:
                for j in range(i, len(nums)):
                    t += dfs(j + 1, nums[j], None)
            elif d is None:
                t += dfs(i + 1, nums[i], nums[i] - n)
            elif n + d == nums[i]:
                t += dfs(i + 1, nums[i], d) + 1

            return t

        return dfs(0, None, None)
