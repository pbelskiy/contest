class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        n = len(pattern)
        matched = []

        for word in words:
            d = {}

            for i, ch in enumerate(word):
                if ch in d and d[ch] != pattern[i]:
                    break
                if ch not in d and pattern[i] in d.values():
                    break

                d[ch] = pattern[i]
            else:
                matched.append(word)

        return matched
