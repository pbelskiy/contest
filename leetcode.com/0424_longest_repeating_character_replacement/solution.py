class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def sw(ch):
            best = 0
            fix = 0
            left = 0

            for right in range(len(s)):
                if s[right] != ch:
                    fix += 1

                while fix > k:
                    if s[left] != ch:
                        fix -= 1
                    left += 1

                best = max(best, right - left + 1)

            return best

        return max(sw(ch) for ch in set(s))
