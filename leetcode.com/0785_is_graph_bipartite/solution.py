"""
https://en.wikipedia.org/wiki/Bipartite_graph

Для того, чтобы проверить граф на предмет двудольности, достаточно в
каждой компоненте связности выбрать любую вершину и помечать оставшиеся
вершины во время обхода графа (например, поиском в ширину) поочерёдно как
чётные и нечётные (см. иллюстрацию).

Если при этом не возникнет конфликта, все чётные вершины образуют
множество U, а все нечётные  V.
"""

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        def bfs(i, m):
            q = collections.deque([i])

            while q:
                i = q.popleft()

                for j in graph[i]:
                    if colors[j] is None:
                        colors[j] = (not colors[i])
                        q.append(j)
                    elif colors[j] is colors[i]:
                        return False

            return True

        colors = [None] * len(graph)
        for i in range(len(graph)):
            if colors[i] is None:
                if not bfs(i, False):
                    return False

        return True
