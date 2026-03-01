class Solution:
    def minCost(self, n: int) -> int:
        t = 0
        p = 0
        x = n

        while x > 0:
            x -= 1
            p += x
            t += 1

            if t == n:
                break

        return p

