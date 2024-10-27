class Solution:
    def possibleStringCount(self, word: str) -> int:
        t = 1

        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                t += 1

        return t
