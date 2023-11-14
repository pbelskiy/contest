"""
Get first and last occurance of each character, then
get unique symbols between them.

TC: O(N)
SC: O(1)
"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first, last = {}, {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
                continue

            last[s[i]] = i

        t = 0
        for ch in last:
            t += len(set(s[first[ch]+1:last[ch]]))

        return t
