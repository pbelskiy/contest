class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        best = 0
        count = Counter()
        left = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            best = max(best, right - left + 1)

        return best
