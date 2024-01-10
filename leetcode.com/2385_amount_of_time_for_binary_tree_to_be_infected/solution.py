class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def dfs(node):
            if node.left:
                g[node.val].append(node.left.val)
                g[node.left.val].append(node.val)
                dfs(node.left)

            if node.right:
                g[node.val].append(node.right.val)
                g[node.right.val].append(node.val)
                dfs(node.right)

        g = defaultdict(list)
        dfs(root)

        q = deque([start])
        v = set([start])
        t = 0
        while q:
            nq = deque()
            while q:
                n = q.popleft()
                for f in g[n]:
                    if f not in v:
                        v.add(f)
                        nq.append(f)

            if nq:
                t += 1
            q = nq

        return t
