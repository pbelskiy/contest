class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        def get_sum(node, s):
            if not node:
                return 0

            node.left_sum = get_sum(node.left, s + node.val)
            node.right_sum = get_sum(node.right, s + node.val)
            return node.val + node.left_sum + node.right_sum

        get_sum(root, 0)

        def get_product(node, parent_sum):
            if not node:
                return 0

            a = node.val + parent_sum + node.right_sum
            b = node.val + parent_sum + node.left_sum
            product = max(a*node.left_sum, b*node.right_sum)

            return max(get_product(node.left, a), get_product(node.right, b), product)

        return get_product(root, 0) % (10**9 + 7)
