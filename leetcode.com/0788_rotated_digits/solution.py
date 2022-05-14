class Solution:
    def rotatedDigits(self, n: int) -> int:
        total = 0

        for v in range(1, n + 1):
            s = set(str(v))

            # if rotatable digits here
            if s - {'0', '1', '8'} and not s & {'3', '4', '7'}:
                total += 1

        return total
