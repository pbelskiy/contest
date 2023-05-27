class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        @cache
        def dfs(s):
            found = False
            m = float('inf')

            for w in dictionary:
                if w in s:
                    found = True
                    m = min(m, dfs(s.replace(w, w.upper())))

            if not found:
                return len([ch for ch in s if ch.lower() == ch])

            return m

        dictionary = [w for w in dictionary if w in s]
        return dfs(s)
