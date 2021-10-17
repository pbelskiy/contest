class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0

        for row in grid:
            for i in reversed(row):
                if i < 0:
                    total += 1
                else:
                    break

        return total
