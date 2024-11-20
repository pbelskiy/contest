"""
Sliding window of unused characters in middle.

TC: O(N)
SC: O(1)
"""
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = Counter(s)
        m = float('inf')

        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1

        left = 0
        for right in range(len(s)):
            count[s[right]] -= 1

            while count[s[right]] < k:
                count[s[left]] += 1
                left += 1

            if count[s[right]] >= k:
                m = min(m, len(s) - (right - left + 1))

        return m
