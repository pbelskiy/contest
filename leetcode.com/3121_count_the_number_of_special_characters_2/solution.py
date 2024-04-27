class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lo, hi = {}, {}

        for i, ch in enumerate(word):
            if ch.islower():
                lo[ch] = i

            if ch.isupper() and ch not in hi:
                hi[ch] = i

        t = 0
        for ch in string.ascii_lowercase:
            if ch in lo and ch.upper() in hi and lo[ch] < hi[ch.upper()]:
                t += 1

        return t
