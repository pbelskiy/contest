class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            if not node:
                return 0, True

            left, left_perfect = dfs(node.left)
            right, right_erfect = dfs(node.right)

            total = left + right + 1
            is_perfect = left == right and left_perfect and right_erfect

            if is_perfect:
                a.append(total)

            return total, is_perfect

        a = []
        dfs(root)

        if len(a) < k:
            return -1

        return sorted(a, reverse=True)[k - 1]
