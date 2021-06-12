from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a = defaultdict(int)
        b = defaultdict(int)

        for c in ransomNote:
            a[c] += 1

        for c in magazine:
            b[c] += 1

        for k, v in a.items():
            if v > b[k]:
                return False

        return True
