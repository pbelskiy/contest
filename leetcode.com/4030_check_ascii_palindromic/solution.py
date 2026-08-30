class Solution:
    def isPalindromic(self, s: str) -> bool:
        a = ''.join(bin(ord(ch))[2:].rjust(8, '0') for ch in s)
        return a[len(a) // 2:] == a[:len(a) // 2][::-1]

