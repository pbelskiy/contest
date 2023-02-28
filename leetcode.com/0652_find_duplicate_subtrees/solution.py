class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def dfs(node):
            if not node:
                return

            h = str(node.val)
            h += 'l' + str(dfs(node.left))
            h += 'r' + str(dfs(node.right))

            d[h].append(node)
            return h

        d = defaultdict(list)
        dfs(root)
        return [v[0] for v in d.values() if len(v) > 1]
