class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        row_changes = 0

        for row in grid:
            for i in range(len(row) // 2):
                if row[i] != row[len(row) - i - 1]:
                    row_changes += 1

        col_changes = 0
        rgrid = list(zip(*grid))
        for row in rgrid:
            for i in range(len(row) // 2):
                if row[i] != row[len(row) - i - 1]:
                    col_changes += 1

        return min(row_changes, col_changes)
