class Solution:
    def integerBreak(self, n: int) -> int:

        def dfs(v):
            if v < 5:
                return v

            return 3*dfs(v - 3)

        if n < 4:
            return n - 1

        return dfs(n)

        #  5 = 3*2 => 6
        #  6 = 3*3 => 9
        #  7 = 3*4 => 12
        #  8 = 3*3*2 => 18
        #  9 = 3*3*3 => 27
        # 10 = 3*3*4 => 36
        # 11 = 3*3*3*2 => 54
        # 12 = 3*3*3*3 => 81
        # 13 = 3*3*3*4 => 108
        # 14 = 3*3*3*3*2 => 162
