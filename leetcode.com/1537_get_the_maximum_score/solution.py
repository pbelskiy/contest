class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def dp(i, j):
            if j == 1 and i == len(nums1):
                return 0
            if j == 2 and i == len(nums2):
                return 0

            m = 0
            if j == 1:
                n = nums1[i]
                if n in d2:  # swtich
                    m = max(m, dp(d2[n] + 1, 2) + n)
                m = max(m, dp(i + 1, j) + n)
            else:
                n = nums2[i]
                if n in d1:  # switch
                    m = max(m, dp(d1[n] + 1, 1) + n)
                m = max(m, dp(i + 1, j) + n)

            return m

        d1, d2 = {}, {}
        for n in set(nums1) & set(nums2):
            d1[n] = bisect.bisect_left(nums1, n)
            d2[n] = bisect.bisect_left(nums2, n)

        return max(dp(0, 1), dp(0, 2)) % (10**9 + 7)
