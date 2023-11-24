class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        def dfs(node, curr_min, curr_max):
            if not node:
                return True, 0, curr_min, curr_max

            left, right, total_sum = True, True, node.val
            l_min, l_max, r_min, r_max = curr_min, curr_max, curr_min, curr_max

            if node.left:
                l_bst, l_sum, l_min, l_max = dfs(node.left, float('inf'), float('-inf'))
                left = l_bst and node.val > max(l_max, l_min)
                total_sum += l_sum

            if node.right:
                r_bst, r_sum, r_min, r_max = dfs(node.right, float('inf'), float('-inf'))
                right = r_bst and node.val < min(r_max, r_min)
                total_sum += r_sum

            if left and right:
                self.best = max(self.best, total_sum)

            is_bst = left and right
            t_min = min(l_min, r_min, node.val)
            t_max = max(l_max, r_max, node.val)
            return is_bst, total_sum, t_min, t_max

        self.best = 0
        dfs(root, root.val, root.val)
        return self.best
