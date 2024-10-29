"""
Process each character by DFS with recursion.

TC: (T)
SC: (N+T)
"""
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        @cache
        def dfs(ch, t):
            d = ord('z') - ord(ch)  # how many steps to became `z`
            if t <= d:
                return 1

            return (dfs('a', t - d - 1) + dfs('b', t - d - 1)) % (10**9 + 7)

        r = 0
        for ch in s:
            r += dfs(ch, t)

        dfs.cache_clear()  # clear after each test case to prevent MLE
        return r % (10**9 + 7)
