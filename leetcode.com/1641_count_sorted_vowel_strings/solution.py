class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ('a', 'e', 'i', 'o', 'u')

        @functools.cache
        def dfs(i, r):
            if r == 0:
                return 1

            total = 0

            for j in range(i, len(vowels)):
                total += dfs(j, r - 1)
            return total

        return dfs(0, n)
