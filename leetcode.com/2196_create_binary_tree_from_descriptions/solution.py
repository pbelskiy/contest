class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        childs = set()
        parents = set()

        for parent, child, left in descriptions:
            childs.add(child)
            parents.add(parent)

            if parent in nodes:
                node = nodes[parent]
            else:
                node = TreeNode(parent)
                nodes[parent] = node

            if child in nodes:
                cnode = nodes[child]
            else:
                cnode = TreeNode(child)
                nodes[child] = cnode

            if left:
                node.left = cnode
            else:
                node.right = cnode

        return nodes[list(parents - childs)[0]]
