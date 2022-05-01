class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        total = 0

        for a, b in zip(s1, s2):
            if a != b:
                total += 1

        return total <= 2 and sorted(s1) == sorted(s2)
