class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        return sum(range(1, s.count(c) + 1))
