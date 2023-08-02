class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        def dfs(i):
            r = d[i].importance

            for s in d[i].subordinates:
                r += dfs(s)

            return r

        d = {}
        for e in employees:
            d[e.id] = e

        return dfs(id)
