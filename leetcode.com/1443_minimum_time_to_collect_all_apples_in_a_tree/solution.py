class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        def dfs(i, p):
            a, s = hasApple[i], 0

            for j in g[i]:
                if j == p:
                    continue

                ca, cs = dfs(j, i)
                cs += 2

                if ca > 0:
                    s += cs
                    a += ca

            return a, s

        return dfs(0, -1)[1]
