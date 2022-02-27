class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(i, p):
            if i == len(graph) - 1:
                paths.append(p)
                return

            for j in graph[i]:
                dfs(j, p + [j])

        paths = []
        dfs(0, [0])
        return paths
