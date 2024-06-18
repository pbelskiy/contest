class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        @cache
        def dp(i):
            m = 0

            for j in range(i + 1, min(i + 1 + d, len(arr))):
                if arr[j] >= arr[i]:
                    break
                m = max(m, dp(j) + 1)

            for j in range(i - 1, max(-1, i - 1 - d), -1):
                if arr[j] >= arr[i]:
                    break
                m = max(m, dp(j) + 1)

            return m

        return max(dp(i) + 1 for i in range(len(arr)))
