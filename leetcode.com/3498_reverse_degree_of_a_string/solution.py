class Solution:
    def reverseDegree(self, s: str) -> int:
        t = 0

        for i, ch in enumerate(s, start=1):
            t += abs(ord(ch) - ord('z') - 1) * i

        return t
