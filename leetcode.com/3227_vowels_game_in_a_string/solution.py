class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        t = 0

        for ch in s:
            if ch in vowels:
                t += 1

        return t != 0
