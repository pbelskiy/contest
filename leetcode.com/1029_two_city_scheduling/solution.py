class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        @functools.cache
        def dfs(i, a, b):
            if i >= len(costs):
                return 0

            if a > 0 and b > 0:
                return min(
                    costs[i][0] + dfs(i + 1, a - 1, b),
                    costs[i][1] + dfs(i + 1, a, b - 1),
                )
            elif a > 0:
                return costs[i][0] + dfs(i + 1, a - 1, b)
            elif b > 0:
                return costs[i][1] + dfs(i + 1, a, b - 1)

        return dfs(0, len(costs) // 2, len(costs) // 2)
