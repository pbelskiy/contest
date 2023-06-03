class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(i):
            return max((dfs(j) + informTime[i] for j in g[i]), default=0)

        g = defaultdict(list)
        for a, b in enumerate(manager):
            g[b].append(a)

        return dfs(headID)
