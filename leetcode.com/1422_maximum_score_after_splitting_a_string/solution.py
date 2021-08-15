class Solution:
    def maxScore(self, s: str) -> int:
        maximum = 0
        ones = 0

        for i in range(len(s)):
            if s[i] == '1':
                ones += 1

        left = 0
        right = ones

        for i in range(len(s) - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1

            maximum = max(maximum, left + right)

        return maximum
