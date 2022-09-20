class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @cache
        def dfs(i, j):
            if i == n1 or j == n2:
                return 0

            return max(
                dfs(i + 1, j + 1) + 1 if text1[i] == text2[j] else 0,
                dfs(i + 1, j),
                dfs(i, j + 1)
            )

        n1, n2 = len(text1), len(text2)
        return dfs(0, 0)
