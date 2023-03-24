"""
TC: O(N) + O(M*N) => O(M*N) where M is valid roots number
"""
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)

        def bfs(i, ban):
            q = deque([i])
            v = set([i])
            while q:
                i = q.popleft()

                for j in g[i]:
                    if (i, j) == ban:
                        continue

                    if j not in v:
                        q.append(j)
                        v.add(j)

            return len(v)

        # collect possible roots
        roots = []
        for i in range(1, len(edges) + 1):
            if bfs(i, None) == len(edges):
                roots.append(i)

        # try to visit all nodes without ban edge using every root
        for ban in reversed(edges):
            for root in roots:
                if bfs(root, tuple(ban)) == len(edges):
                    return ban
