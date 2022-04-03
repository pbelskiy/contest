class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        total = 0

        for a, b in zip(bin(start)[2:].rjust(32, '0'), bin(goal)[2:].rjust(32, '0')):
            if a != b:
                total += 1

        return total
