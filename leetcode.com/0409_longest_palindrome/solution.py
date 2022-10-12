class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        carry = 0

        for v in Counter(s).values():
            if v % 2 == 0:
                longest += v
            else:
                longest += v - 1
                carry = 1

        return longest + carry
