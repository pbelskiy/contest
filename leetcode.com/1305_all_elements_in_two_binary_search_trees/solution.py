class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        numbers = []

        def bfs(node):
            if not node:
                return
            numbers.append(node.val)
            bfs(node.left)
            bfs(node.right)

        bfs(root1)
        bfs(root2)
        return sorted(numbers)
