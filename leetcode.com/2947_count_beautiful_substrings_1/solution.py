class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total = 0

        for i in range(len(s)):
            v, c = 0, 0
            for j in range(i, len(s)):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1

                if v == c and (v * c) % k == 0:
                    total += 1

        return total
