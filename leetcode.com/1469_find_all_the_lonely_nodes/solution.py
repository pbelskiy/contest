"""
1469. Find All The Lonely Nodes (Easy)

In a binary tree, a lonely node is a node that is the only child
of its parent node. The root of the tree is not lonely because it
does not have a parent node.

Given the root of a binary tree, return an array containing the
values of all lonely nodes in the tree. Return the list in any order.

Input:  root = [1,2,3,null,4]
Output: [4]

Explanation: Light blue node is the only lonely node.
Node 1 is the root and is not lonely.
Nodes 2 and 3 have the same parent and are not lonely.
"""
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):

            if node.left and node.right:
                dfs(node.left)
                dfs(node.right)
            elif node.left:
                r.append(node.left.val)
                dfs(node.left)
            elif node.right:
                r.append(node.right.val)
                dfs(node.right)

        r = []
        dfs(root)
        return r
