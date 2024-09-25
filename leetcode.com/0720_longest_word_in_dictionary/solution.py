class Solution:
    def longestWord(self, words: List[str]) -> str:

        def dfs(w):
            if not w:
                return True

            if w not in s:
                return False

            return dfs(w[:-1])

        s = set(words)
        r = []

        for w in words:
            if dfs(w):
                r.append(w)

        if not r:
            return ''

        return sorted(r, key=lambda w: (-len(w), w))[0]
