class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        weight = dict()
        for i, connections in sorted(graph.items(), key=lambda k: len(k[1]), reverse=True):
            weight[i] = n
            n -= 1

        total = 0
        for a, b in roads:
            total += weight[a] + weight[b]

        return total
