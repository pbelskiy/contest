class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = 0

        if low % 2 == 1:
            total += 1
            low += 1

        if high % 2 == 1:
            total += 1
            high -= 1

        total += (high - low) // 2

        return total
