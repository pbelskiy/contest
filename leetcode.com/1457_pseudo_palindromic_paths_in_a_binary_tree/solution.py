class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if not node:
                return 0

            total = 0
            count[node.val] += 1

            if node.left is node.right is None:
                odd = 0
                for n in count:
                    if n % 2 == 1:
                        odd += 1
                if odd < 2:
                    total += 1

            total += dfs(node.left) + dfs(node.right)
            count[node.val] -= 1
            return total

        count = [0]*10
        return dfs(root)
