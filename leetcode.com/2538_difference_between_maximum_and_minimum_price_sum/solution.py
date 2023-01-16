class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        @cache
        def dfs(i, p):
            r = 0

            for j in g[i]:
                if j == p:
                    continue

                r = max(r, dfs(j, i) + price[j])

            return r

        """
        Here we just use DFS to get max sum from target node with
        cache which boost our search.

        min = price[i]
        result = dfs(i, 1) + price[i] - min

        DFS return sum without target node value, so we need to add it,
        also we need to substract minimum from path which supposed to be also
        node value, not last node because it's optimization, because we will process
        from last node to target in future.

        Example:
        [1 + 2 + 3] : (2 + 3) + 1 - 1
                        DFS    val min

        [3 + 2 + 1] : (2 + 1) + 3 - 3
                        DFS    val min

        So we just use result of DFS :-)
        """
        res = float('-inf')
        for i in range(n):
            res = max(res, dfs(i, -1))

        return res
