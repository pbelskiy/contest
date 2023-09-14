"""
Here we build the graph, sort adjacent vertices lexicographically,
and then just start DFS, first path will be the answer.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        def dfs(path):
            if len(path) - 1 == len(tickets):
                return path

            for a in graph[path[-1]]:
                k = path[-1], a

                if count[k] > 0:
                    count[k] -= 1
                    res = dfs(path + (a,))
                    if res:
                        return res
                    count[k] += 1

            return False

        graph = defaultdict(set)
        count = Counter()

        for a, b in tickets:
            graph[a].add(b)
            count[(a, b)] += 1

        for k, v in graph.items():
            graph[k] = sorted(v)

        return dfs(('JFK',))
