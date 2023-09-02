class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        f1, f2 = Counter(), Counter()

        for i in range(0, len(s1), 2):
            f1[s1[i]] += 1
            f1[s2[i]] -= 1

        for i in range(1, len(s1), 2):
            f2[s1[i]] += 1
            f2[s2[i]] -= 1

        if any(f1.values()) or any(f2.values()):
            return False

        return True
