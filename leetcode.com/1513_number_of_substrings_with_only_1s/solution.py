class Solution:
    def numSub(self, s: str) -> int:
        total = 0

        for part in s.split('0'):
            for i in range(1, len(part) + 1):
                total += i

        return total % (10**9 + 7)
