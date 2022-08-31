class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(i, a):
            if i == len(nums):
                s = 0
                for v in a:
                    s ^= v
                self.xs += s
                return

            dfs(i + 1, a)
            dfs(i + 1, a + [nums[i]])

        self.xs = 0
        dfs(0, [])
        return self.xs
