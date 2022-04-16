class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = s[:len(s) // 2].lower(), s[len(s) // 2:].lower()
        n1, n2 = 0, 0

        for ch in 'aeiou':
            n1 += a.count(ch)
            n2 += b.count(ch)

        return n1 == n2
