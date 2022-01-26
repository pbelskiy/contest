class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node, d):
            if not node:
                return

            levels[d].append(node.val)

            bfs(node.left, d + 1)
            bfs(node.right, d + 1)

        if not root:
            return []

        levels = collections.defaultdict(list)
        bfs(root, 0)

        return [levels[i] if i % 2 == 0 else reversed(levels[i]) for i in range(max(levels) + 1)]
