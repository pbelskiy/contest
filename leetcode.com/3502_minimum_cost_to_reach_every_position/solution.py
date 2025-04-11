class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        a = []

        m = cost[0]

        for n in cost:
            m = min(m, n)
            a.append(m)

        return a

