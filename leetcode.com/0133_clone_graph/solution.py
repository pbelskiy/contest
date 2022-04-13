class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        def dfs(a):
            if not a:
                return

            r = Node(a.val)
            d[a] = r

            if a.neighbors is not None:
                for b in a.neighbors:
                    if b in d:
                        r.neighbors.append(d[b])
                    else:
                        c = dfs(b)
                        if not c:
                            continue
                        r.neighbors.append(c)

            return r

        d = {}
        return dfs(node)
