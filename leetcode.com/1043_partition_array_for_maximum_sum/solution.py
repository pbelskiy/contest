class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        @cache
        def dfs(i):
            if i == len(arr):
                return 0

            m = 0
            v = arr[i]

            for j in range(i, min(i + k, len(arr))):
                v = max(v, arr[j])
                n = j - i + 1
                m = max(m, dfs(j + 1) + v*n)

            return m

        return dfs(0)
