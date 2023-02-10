class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        limit = 100

        for ch in s:
            idx = ord(ch) - ord('a')

            if limit - widths[idx] < 0:
                lines += 1
                limit = 100

            limit -= widths[idx]

        return [lines, 100 - limit]
