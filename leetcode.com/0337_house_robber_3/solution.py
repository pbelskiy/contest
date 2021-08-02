class Solution:

    def rob(self, root):

        @functools.cache
        def dfs(node, take):
            if not node:
                return 0

            val = node.val if take else 0

            variants = (
                (not take, not take),
                (not take, False),
                (False, not take),
                (False, False),
            )

            v = val
            for t1, t2 in variants:
                v = max(v, val + dfs(node.left, t1) + dfs(node.right, t2))
            return v

        return max(dfs(root, False), dfs(root, True))
