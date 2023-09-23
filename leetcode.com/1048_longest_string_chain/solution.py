class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def is_predecessor(a, b):
            i = 0
            for ch in a:
                while True:
                    if i < len(b) and b[i] == ch:
                        i += 1
                        break

                    if i == len(b):
                        return False
                    i += 1

            return True

        @cache
        def dfs(w):
            best = 0
            for n in d[len(w) + 1]:
                if is_predecessor(w, n):
                    best = max(best, dfs(n) + 1)
            return best

        d = defaultdict(list)
        for w in words:
            d[len(w)].append(w)

        return max(dfs(w) + 1 for w in words)
