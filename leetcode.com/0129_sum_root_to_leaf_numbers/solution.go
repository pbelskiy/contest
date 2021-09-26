func dfs(node *TreeNode, total int) int {
    if node.Left == nil && node.Right == nil {
        return total*10 + node.Val
    }

    v := 0

    if node.Left != nil {
        v += dfs(node.Left, total*10 + node.Val)
    }

    if node.Right != nil {
        v += dfs(node.Right, total*10 + node.Val)
    }

    return v
}

func sumNumbers(root *TreeNode) int {
    return dfs(root, 0)
}
