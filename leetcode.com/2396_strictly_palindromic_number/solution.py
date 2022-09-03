class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:

        def get(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]

        for b in range(2, n - 2 + 1):
            a = get(n, b)
            if a != a[::-1]:
                return False

        return True
