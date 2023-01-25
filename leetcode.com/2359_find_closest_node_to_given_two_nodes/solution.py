# 15 min, using mobile phone

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        def dfs(i, d, a):
            if i == -1 or i in a:
                return
            a[i] = d
            dfs(edges[i], d + 1, a)

        # find distance to nodes
        n1 = {}
        n2 = {}

        dfs(node1, 0, n1)
        dfs(node2, 0, n2)

        # find common and sort
        r = []
        for n, d in n1.items():
            if n not in n2:
                continue
            r.append((max(d, n2[n]), n))

        if not r:
            return -1

        r.sort()
        return r[0][1]
