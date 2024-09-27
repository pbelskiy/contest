class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        @cache
        def dfs(i, j):
            if i == len(a):
                return 0

            if j == len(b):
                return float('-inf')

            return max(
                dfs(i + 1, j + 1) + a[i] * b[j],  # pick
                dfs(i, j + 1),                    # not pick
            )

        gc.collect()  # without it I got MLE on contest because of huge cache and GC in Python
        return dfs(0, 0)
