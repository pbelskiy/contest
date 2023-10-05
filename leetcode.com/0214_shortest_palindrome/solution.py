class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s), -1, -1):   # try to add reversed prefix from end
            r = s[i:][::-1] + s
            if r == r[::-1]:              # is new string palindrome
                return r
