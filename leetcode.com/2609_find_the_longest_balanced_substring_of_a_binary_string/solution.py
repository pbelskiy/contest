class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        m = 0

        for i in range(len(s) - 1):
            if not (s[i] == '0' and s[i + 1] == '1'):
                continue

            left, right = i, i + 1

            while ((left - 1 >= 0 and right + 1 < len(s)) and
                   (s[left - 1] == '0' and s[right + 1] == '1')):
                left -= 1
                right += 1

            m = max(m, right - left + 1)

        return m
