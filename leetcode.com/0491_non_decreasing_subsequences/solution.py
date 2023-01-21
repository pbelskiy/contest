class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, a):
            if i == len(nums):
                return

            for j in range(i, len(nums)):
                if a and a[-1] > nums[j]:
                    continue
                na = a[:] + [nums[j]]
                if len(na) > 1:
                    res.add(tuple(na))
                dfs(j + 1, na)

        res = set()
        dfs(0, [])
        return res
