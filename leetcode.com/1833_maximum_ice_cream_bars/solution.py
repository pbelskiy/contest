class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        s, i = 0, 0

        while i < len(costs):
            if s + costs[i] > coins:
                break

            s += costs[i]
            i += 1

        return i
