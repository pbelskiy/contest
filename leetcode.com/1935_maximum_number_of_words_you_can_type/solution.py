class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = 0
        b = set(brokenLetters)

        for w in text.split():
            if not (set(w) & b):
                t += 1

        return t
