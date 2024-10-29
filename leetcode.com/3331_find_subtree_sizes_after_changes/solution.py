"""
Do what asked.
1) Collect needed changes
2) Make changes
3) Count subtrees size using second dfs

TC: O(N)
SC: O(N)
"""
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        def dfs2(a):
            t = 1
            for b in g[a]:
                t += dfs2(b)
            res[a] = t
            return t

        def dfs(a, p, closest):
            new = closest.get(s[a])
            if new is not None and new != p:
                changes[a] = (p, new)

            prev = closest.get(s[a])
            closest[s[a]] = a
            for b in g[a]:
                dfs(b, a, closest)
            closest[s[a]] = prev

        # consturct graph
        g = defaultdict(set)
        for i in range(len(parent)):
            g[parent[i]].add(i)

        # collect needed changes
        changes = {}
        dfs(0, None, {})

        # make changes
        for node, (prev, new) in changes.items():
            g[prev].remove(node)
            g[new].add(node)

        # count subtrees size
        res = [0]*len(parent)
        dfs2(0)
        return res
