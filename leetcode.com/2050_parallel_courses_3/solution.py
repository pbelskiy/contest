class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        @cache
        def dfs(i):
            if not g[i]:
                return time[i - 1]

            m = 0
            for j in g[i]:
                m = max(m, dfs(j))

            return m + time[i - 1]

        g = defaultdict(list)
        for i, j in relations:
            g[j].append(i)

        return max(dfs(i) for i in range(1, n + 1))
