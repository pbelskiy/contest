class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return ''.join(sorted(s, reverse=x < y))

