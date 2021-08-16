class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        length = len(cost)
        val = cost[:]

        for i in range(2, length):
            val[i] = min(val[i - 1] + cost[i], val[i - 2] + cost[i])

        return min(val[length - 1], val[length - 2])
