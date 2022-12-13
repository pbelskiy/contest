class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(i):
            if i == len(s):
                return True

            for w in wordDict:
                if s[i:].startswith(w) and dfs(i + len(w)):
                    return True

            return False

        return dfs(0)
