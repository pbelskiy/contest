class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        O(N^2), just find max length of any possible palindromes.
        """
        def get(left, right):
            length = right - left - 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break

                length, left, right = length + 2, left - 1, right + 1

            return length, left, right

        m, l, r = 0, 0, 0
        for i in range(len(s)):
            m, l, r = max((m, l, r), get(i - 1, i + 1),  get(i - 1, i))

        return s[l+1:r]
