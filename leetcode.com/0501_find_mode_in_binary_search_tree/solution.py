class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            if not node:
                return

            cnt[node.val] += 1

            dfs(node.left)
            dfs(node.right)

        cnt = collections.Counter()
        dfs(root)
        t = cnt.most_common(1)[0][1]
        return [k for k, v in cnt.items() if v == t]
