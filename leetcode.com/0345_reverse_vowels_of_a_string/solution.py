class Solution:
    def reverseVowels(self, s: str) -> str:
        VOWELS = ('a', 'e', 'i', 'o', 'u')

        a = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if a[left].lower() not in VOWELS:
                left += 1
                continue

            if a[right].lower() not in VOWELS:
                right -= 1
                continue

            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

        return ''.join(a)
