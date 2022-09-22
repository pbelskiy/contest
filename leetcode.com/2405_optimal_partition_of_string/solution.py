class Solution:
    def partitionString(self, s: str) -> int:
        count, chars = 0, set()

        for ch in s:
            if ch in chars:
                count += 1
                chars = set()
            chars.add(ch)

        if chars:
            count += 1

        return count
