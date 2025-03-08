class Solution:
    def minCost(self, nums: List[int]) -> int:

        @cache
        def dfs(i, j):
            if j != -1:
                d = 2
                indices = [j] + list(range(i, min(i + d, len(nums))))
            else:
                d = 3
                indices = list(range(i, min(i + d, len(nums))))

            if len(indices) < 3:
                return max([nums[x] for x in indices], default=0)

            return min(
                dfs(i + d, indices[0]) + max(nums[indices[1]], nums[indices[2]]),
                dfs(i + d, indices[1]) + max(nums[indices[0]], nums[indices[2]]),
                dfs(i + d, indices[2]) + max(nums[indices[0]], nums[indices[1]]),
            )

        return dfs(0, -1)
