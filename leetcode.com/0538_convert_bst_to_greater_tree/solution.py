class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs_get(node):
            if not node:
                return
            nums.append(node.val)
            dfs_get(node.left)
            dfs_get(node.right)

        def dfs_set(node):
            if not node:
                return

            node.val += s[node.val]

            dfs_set(node.left)
            dfs_set(node.right)

        nums = []
        dfs_get(root)
        nums.sort()

        s = {}

        for i, n in enumerate(nums):
            s[n] = sum(nums[i+1:])

        dfs_set(root)
        return root
