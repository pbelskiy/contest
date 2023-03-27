"""
TC: O(N)
SC: O(1)
"""
class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        longest = 0

        left = 0
        while left < len(word):
            right = left
            for ch in ('a', 'e', 'i', 'o', 'u'):
                if right < len(word) and word[right] != ch:
                    if ch == 'a':
                        right += 1
                    break

                while right < len(word) and word[right] == ch:
                    right += 1

            else:
                if right <= len(word) and word[right - 1] == 'u':
                    longest = max(longest, right - left)

            left = right

        return longest
