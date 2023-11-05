class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        w = 0
        t = float('-inf')

        for i, row in enumerate(grid):
            if sum(row) >= t:
                w = i
                t = sum(row)

        return w
