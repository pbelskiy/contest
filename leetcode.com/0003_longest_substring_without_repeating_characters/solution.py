class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        max_len = 0
        left = -1

        for pos, ch in enumerate(s):
            if ch in h:
                left = max(left, h[ch])

            h[ch] = pos
            max_len = max(max_len, pos - left)

        return max_len
