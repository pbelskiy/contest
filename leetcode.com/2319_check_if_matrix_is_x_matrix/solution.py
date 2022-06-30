class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        total = sum(map(sum, grid))
        tdiag = 0

        for d in range(len(grid)):
            v1 = grid[d][d]
            v2 = grid[len(grid) - 1 - d][d]
            if v1 == 0 or v2 == 0:
                return False

            if d == len(grid) - 1 - d:
                v2 = 0

            tdiag += v1 + v2

        return (total - tdiag) == 0
