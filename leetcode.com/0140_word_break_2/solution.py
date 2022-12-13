class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def dfs(i, v):
            if i == len(s):
                self.a.append(v[1:])
                return

            for w in wordDict:
                if s[i:].startswith(w):
                    dfs(i + len(w), v + ' ' + w)

        self.a = []
        dfs(0, '')
        return self.a
