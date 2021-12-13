class Solution:
    def maxPower(self, s: str) -> int:
        power, total = 1, 1

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                total += 1
            else:
                power = max(power, total)
                total = 1

        return max(power, total)
