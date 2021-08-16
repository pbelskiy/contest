class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        val = [0] * n
        val[0] = 2
        val[1] = 3

        for i in range(2, n):
            val[i] = val[i - 1] + val[i - 2]

        return val[n - 2]
