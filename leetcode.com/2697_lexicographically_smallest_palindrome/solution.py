class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)

        left, right = 0, len(a) - 1

        while left < right:
            a[left] = a[right] = min(a[left], a[right])
            left += 1
            right -= 1

        return ''.join(a)
