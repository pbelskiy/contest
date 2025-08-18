class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        for yy in range(y, y + k):
            a = []
            for d in range(k):
                a.append(grid[x + d][yy])

            for d in range(k):
                grid[x + d][yy] = a.pop()

        return grid

