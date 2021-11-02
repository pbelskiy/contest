class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[int(not obstacleGrid[i][j]) for j in range(n)] for i in range(m)]

        for i in range(1, m):
            if dp[i - 1][0] == 0:
                dp[i][0] = 0

        for j in range(1, n):
            if dp[0][j - 1] == 0:
                dp[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
