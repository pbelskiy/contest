class Solution:
    def coloredCells(self, n: int) -> int:
        return 1 + 4*sum(range(n))
