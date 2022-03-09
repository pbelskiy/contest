class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        for a, b in edges:
            d[b].append(a)

        @functools.cache
        def dfs(i, j):
            if i not in d:
                return

            for n in d[i]:
                s.add(n)
                dfs(n, j)
      
        values = []
        for i in range(n):
            s = set()
            dfs(i, i)
            values.append(sorted(s))

        return values
