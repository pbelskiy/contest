class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1, s2 = a.bit_count(), b.bit_count()

        if s1 >= s2:
            return s1 * s2

        return s2 // s1

