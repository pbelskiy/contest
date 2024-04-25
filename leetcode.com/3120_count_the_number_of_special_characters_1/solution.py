class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        t = 0

        for ch in string.ascii_lowercase:
            if ch in word and ch.upper() in word:
                t += 1

        return t
