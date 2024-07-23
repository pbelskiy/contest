class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:

        def dfs(n):
            if n.left:
                v = n.left.val
                g[n.val].append(v)
                g[v].append(n.val)
                d[(n.val, v)] = "L"
                d[(v, n.val)] = "U"
                dfs(n.left)

            if n.right:
                v = n.right.val
                g[n.val].append(v)
                g[v].append(n.val)
                d[(n.val, v)] = "R"
                d[(v, n.val)] = "U"
                dfs(n.right)

        g = defaultdict(list)
        d = {}
        dfs(root)

        q = deque([(startValue, "")])
        v = set()
        while q:
            a, p = q.popleft()
            if a == destValue:
                return p
            for b in g[a]:
                if (a, b) not in v:
                    v.add((a, b))
                    q.append((b, p + d[(a, b)]))
