class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total = 0

        for i in range(0, len(cost), 3):
            if i + 1 < len(cost):
                total += cost[i] + cost[i + 1]
            else:
                total += cost[i]
        
        return total
