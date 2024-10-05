"""
My first idea was DP with two passes for first robot and
after erase first robot path, calculate the second robot
score value, but that greedy approach doesn't work here.

So then need to try all possible paths for first robot,
erase cells, and then get max possible value for second
robot path after.

So we can do brute force which leeds to TLE, but using
prefix sum here is more effective, just check in second
cycle where first robot goes down, then get the better
value of possible paths for second robot.

TC: O(N)
SC: O(1)
"""
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        w = len(grid[0])

        # calculate prefix sum
        for i in range(1, w):
            grid[0][i] += grid[0][i - 1]
            grid[1][i] += grid[1][i - 1]

        # get best answer
        m = float('inf')
        for i in range(w):
            a = grid[0][-1] - grid[0][i]        # top line score
            b = grid[1][i - 1] if i > 0 else 0  # bottom line score

            m = min(m, max(a, b))

        return m
