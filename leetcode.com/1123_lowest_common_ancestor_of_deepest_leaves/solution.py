class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # collect layers
        q = [(root, None)]
        while q:
            nq = []
            latest = q[:]
            while q:
                n, p = q.pop()
                n.p = p

                if n.left:
                    nq.append((n.left, n))
                if n.right:
                    nq.append((n.right, n))

            q = nq

        # find near common parent
        if len(latest) == 1:
            return latest[0][0]

        parents = [n[1] for n in latest]
        while len(set(parents)) > 1:
            parents = [n.p for n in parents]

        return parents[0]
