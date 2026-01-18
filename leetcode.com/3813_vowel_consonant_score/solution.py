class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        v = 0
        c = 0
        for ch in s:
            if ch in vowels:
                v += 1
            elif not ch.isdigit() and ch != ' ':
                c += 1

        if c == 0:
            return 0

        return math.floor(v / c)

