"""
Just find here minimum cost to transform a -> b using BFS.
"""
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str],
                          changed: List[str], cost: List[int]) -> int:

        @cache
        def bfs(a, b):
            q = [(0, a)]
            v = set()
            while q:
                total, char = heappop(q)
                if char == b:
                    return total

                for ch, cst, i in d[char]:
                    if i not in v:
                        heappush(q, (total + cst, ch))
                        v.add(i)

            return -1

        d = defaultdict(list)
        for i in range(len(cost)):
            d[original[i]].append((changed[i], cost[i], i))

        t = 0
        for a, b in zip(source, target):
            if a == b:
                continue

            v = bfs(a, b)
            if v == -1:
                return -1
            t += v

        return t
