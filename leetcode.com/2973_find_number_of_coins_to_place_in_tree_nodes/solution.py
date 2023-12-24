class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(i, p):
            vals = [cost[i]]
            for j in g[i]:
                if j == p:
                    continue
                vals.extend(dfs(j, i))

            vals.sort()
            if len(vals) >= 3:
                result[i] = max(
                    0,
                    vals[0] * vals[1] * vals[-1],
                    vals[-1] * vals[-2] * vals[-3],
                )

            return vals

        result = [1]*len(cost)
        dfs(0, -1)
        return result
