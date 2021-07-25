class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0

        for i, ch in enumerate(reversed(columnTitle)):
            v = ord(ch) - ord('A') + 1
            total += v * 26**i

        return total
