class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a, m = 0, 0

        for d in gain:
            a += d
            m = max(m, a)

        return m
