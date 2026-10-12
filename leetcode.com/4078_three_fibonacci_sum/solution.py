class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a, b, c = 0, 1, 1

        while a + b + c <= n:
            if a + b + c == n:
                return True
            a, b, c = b, c, b + c

        return False

