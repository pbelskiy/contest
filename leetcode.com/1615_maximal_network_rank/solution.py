class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(set)

        for a, b in roads:
            t = (min(a, b), max(a, b))
            d[a].add(t)
            d[b].add(t)

        m = 0
        for a, b in combinations(d.keys(), 2):
            m = max(m, len(d[a] | d[b]))

        return m
