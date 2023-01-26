class Solution:
    def findCheapestPrice(self, n: int, flights, src: int, dst: int, k: int) -> int:
        dirs = defaultdict(list)
        cost = {}

        for a, b, c in flights:
            dirs[a].append(b)
            cost[(a, b)] = c

        @cache
        def dfs(i, r):
            if i == dst:
                return 0

            if r < 0:
                return float('inf')

            v = float('inf')
            for j in dirs[i]:
                v = min(v, dfs(j, r - 1) + cost[(i, j)])
            return v

        r = dfs(src, k)
        if r == float('inf'):
            return -1
        return r
