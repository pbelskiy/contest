class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        a1, a2 = sorted(s1), sorted(s2)

        for a, b in zip(a1, a2):
            if a < b:
                break
        else:
            return True

        for a, b in zip(a1, a2):
            if b < a:
                break
        else:
            return True

        return False
