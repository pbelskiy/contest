class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dfs(i, j, l):
            if i == len(nums1) or j == len(nums2):
                if l == 0:
                    return nums1[-1]*nums2[-1]
                return 0

            return max(
                dfs(i + 1, j + 1, 1) + nums1[i]*nums2[j],
                dfs(i + 1, j, max(0, l)),
                dfs(i, j + 1, max(0, l)),
            )

        return dfs(0, 0, 0)
