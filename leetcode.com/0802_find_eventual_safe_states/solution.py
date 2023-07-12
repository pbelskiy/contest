class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        @cache
        def dfs(i):
            v[i] = 'start'

            for j in graph[i]:
                if j not in v and not dfs(j):
                    return False

                # cycle found
                if v[j] == 'start':
                    return False

            v[i] = 'finished'
            return True

        v = {}
        return [i for i in range(len(graph)) if dfs(i)]
