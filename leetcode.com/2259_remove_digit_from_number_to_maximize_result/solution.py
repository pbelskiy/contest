class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        values = []

        for i, n in enumerate(number):
            if n == digit:
                values.append(number[:i] + number[i+1:])

        return max(values)
