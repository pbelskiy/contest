class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ways = 1

        if cost1 > cost2:
            cost1, cost2 = cost2, cost1

        for i in range(total // cost1):
            ways += 1 + (total - i * cost1) // cost2

        return ways
