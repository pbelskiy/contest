
class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:

        @cache
        def dp(i, l, r):
            if i == len(words):
                return 0

            m = min(
                dp(i + 1, l, words[i][-1]) + len(words[i]),
                dp(i + 1, words[i][0], r) + len(words[i]),
            )

            if words[i][0] == r:
                m = min(m, dp(i + 1, l, words[i][-1]) + len(words[i]) - 1)

            if words[i][-1] == l:
                m = min(m, (dp(i + 1, words[i][0], r) + len(words[i]) - 1))

            return m

        return dp(1, words[0][0], words[0][-1]) + len(words[0])
