class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        a = [ord(ch) - ord('a') for ch in word]
        n = len(word)
        t = 0

        i = 0
        while i < n - 1:
            if abs(a[i] - a[i + 1]) <= 1:
                t += 1
                i += 2
            else:
                i += 1

        return t
