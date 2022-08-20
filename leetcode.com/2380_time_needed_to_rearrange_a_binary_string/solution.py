class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        total = 0

        while '01' in s:
            s = s.replace('01', '10')
            total += 1

        return total
