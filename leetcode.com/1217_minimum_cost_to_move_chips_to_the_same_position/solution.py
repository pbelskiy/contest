class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        total = [0, 0]

        for p in position:
            total[p % 2] += 1

        return min(total)
