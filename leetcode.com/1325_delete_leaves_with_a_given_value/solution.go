func dfs(node *TreeNode, target int) bool {
    if node == nil {
        return false
    }

    if node.Left == nil && node.Right == nil {
        return node.Val == target
    }

    if dfs(node.Left, target) {
        node.Left = nil
    }

    if dfs(node.Right, target) {
        node.Right = nil
    }

    return node.Left == nil && node.Right == nil && node.Val == target
}

func removeLeafNodes(root *TreeNode, target int) *TreeNode {
    if dfs(root, target) {
        return nil
    }

    return root
}
