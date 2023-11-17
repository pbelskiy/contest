class Solution:
    def isThree(self, n: int) -> bool:
        t = 0

        for d in range(n, 0, -1):
            if n % d == 0:
                t += 1

        return t == 3
