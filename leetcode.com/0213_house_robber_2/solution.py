class Solution:
    def rob(self, nums: List[int]) -> int:

        @cache
        def dfs1(i):
            return max([dfs1(j + 2) + nums1[j] for j in range(i, len(nums1))], default=0)

        @cache
        def dfs2(i):
            return max([dfs2(j + 2) + nums2[j] for j in range(i, len(nums2))], default=0)

        nums1 = nums[:-1]
        v1 = dfs1(0)

        nums2 = nums[1:]
        v2 = dfs2(0)

        return max(nums[0], v1, v2)
