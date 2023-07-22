class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ('a', 'e', 'i', 'o', 'u')

        a = list(s)
        v = sorted([ch for ch in a if ch.lower() in vowels])

        j = 0
        for i in range(len(a)):
            if a[i].lower() in vowels:
                a[i] = v[j]
                j += 1

        return ''.join(a)
