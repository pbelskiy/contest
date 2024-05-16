class Solution:
    def makeFancyString(self, s: str) -> str:
        changed = True
        while changed:
            changed = False
            for ch in string.ascii_lowercase:
                if ch*3 in s:
                    changed = True
                    s = s.replace(ch*3, ch*2)

        return s
