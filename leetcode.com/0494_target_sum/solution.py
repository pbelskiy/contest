class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def dfs(i, s):
            if i == len(nums):
                return int(s == target)

            total = 0

            # minus
            key = (i + 1, s - nums[i])
            if key not in cache:
                cache[key] = dfs(*key)
            total += cache[key]

            # plus
            key = (i + 1, s + nums[i])
            if key not in cache:
                cache[key] = dfs(*key)
            total += cache[key]

            return total

        cache = {}
        return dfs(0, 0)
