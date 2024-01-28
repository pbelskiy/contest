class Solution:
    def countKeyChanges(self, s: str) -> int:
        t = 0
        p = s[0].lower()

        for ch in s:
            if ch.lower() != p:
                t += 1
            p = ch.lower()

        return t
