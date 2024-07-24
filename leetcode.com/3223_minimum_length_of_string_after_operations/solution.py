"""
Count freq of each character, then calculate result.

TC: O(N)
SC: O(N)
"""
class Solution:
    def minimumLength(self, s: str) -> int:
        t = 0

        for v in Counter(s).values():
            if v % 2 == 0:
                t += 2
            else:
                t += 1

        return t
