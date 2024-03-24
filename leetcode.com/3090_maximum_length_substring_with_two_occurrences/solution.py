class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = Counter()
        maximum = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            maximum = max(maximum, right - left + 1)

        return maximum
