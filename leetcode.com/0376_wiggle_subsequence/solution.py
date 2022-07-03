class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        @cache
        def dfs(i, d):
            v = [1]
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j] and d is True:
                    v.append(dfs(j, False) + 1)
                if nums[i] < nums[j] and d is False:
                    v.append(dfs(j, True) + 1)
            return max(v)

        return max(dfs(0, True), dfs(0, False))
