class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, s):
            if i == len(nums):
                self.res.append(s)
                return

            dfs(i + 1, s[:] + [nums[i]])
            dfs(i + 1, s[:])

        self.res = []
        dfs(0, [])
        return self.res
