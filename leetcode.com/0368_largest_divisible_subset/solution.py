"""
Recursion with cache with path as result.

TC: O(N^2)
SC: O(N^2)
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        @cache
        def dfs(i, j):
            if j >= len(nums):
                return []

            p = []

            # pick
            if (nums[i] % nums[j] == 0) or (nums[j] % nums[i] == 0):
                pp = dfs(j, j + 1)
                p = [nums[j]] + pp

            # skip
            pp = dfs(i, j + 1)
            if len(pp) > len(p):
                p = pp

            return p

        nums.sort()

        p = [nums[0]]

        for i in range(len(nums)):
            pp = dfs(i, i + 1)
            if len(pp) >= len(p):
                p = [nums[i]] + pp

        return p

