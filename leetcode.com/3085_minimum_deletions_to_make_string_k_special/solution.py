class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        @cache
        def dfs(left, right):
            d = a[right] - a[left]
            if d <= k:
                return 0

            return min(
                dfs(left + 1, right) + a[left],  # remove
                dfs(left, right - 1) + d - k,    # reduce
            )

        a = sorted(Counter(word).values())
        return dfs(0, len(a) - 1)
