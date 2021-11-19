class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        d = 0

        for i in range(32):
            if ((x >> i) & 1) != ((y >> i) & 1):
                d += 1

        return d
