"""
Ugly solution with convertation from tree to graph and BFS
from each leaf to leaf.

Time: 45 minutes
TC: O(nodes*leaves)
SC: O(nodes)
"""

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def dfs(node):
            if node.left:
                g[id(node)].append(id(node.left))
                g[id(node.left)].append(id(node))
                dfs(node.left)

            if node.right:
                g[id(node)].append(id(node.right))
                g[id(node.right)].append(id(node))
                dfs(node.right)

            if node.left is node.right is None:
                leaves.add(id(node))

        def bfs(t):
            q = deque([(t, 0)])
            v = set([t])

            while q:
                i, d = q.popleft()

                if i != t and i in leaves and d <= distance:
                    if not ((t, i) in pairs or (i, t) in pairs):
                        pairs.add((t, i))

                for j in g[i]:
                    if j not in v:
                        v.add(j)
                        q.append((j, d + 1))

        leaves = set()
        g = defaultdict(list)
        dfs(root)

        pairs = set()
        for leaf in leaves:
            bfs(leaf)

        return len(pairs)
