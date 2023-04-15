class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, p, d):
            if not node:
                return

            vals[d] += node.val
            pars[d][hash(p)] += node.val
            dfs(node.left, node, d + 1)
            dfs(node.right, node, d + 1)

        vals = defaultdict(int)
        pars = defaultdict(lambda: defaultdict(int))
        dfs(root, 0, 0)

        def modify(node, p, d):
            if not node:
                return

            s = vals[d] - pars[d][p]
            orig = hash(node)
            node.val = s

            modify(node.left, orig, d + 1)
            modify(node.right, orig, d + 1)

        modify(root, 0, 0)
        return root
