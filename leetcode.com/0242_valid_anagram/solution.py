class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}

        for c in s:
            sd.setdefault(c, 0)
            sd[c] += 1

        for c in t:
            td.setdefault(c, 0)
            td[c] += 1

        return sd == td

