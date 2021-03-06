func solve(node *TreeNode, v int, d int) {
    if node == nil {
        return
    }

    if (d == 2) {
        node.Left = &TreeNode{Val: v, Left: node.Left}
        node.Right = &TreeNode{Val: v, Right: node.Right}
    } else {
        solve(node.Left, v, d - 1)
        solve(node.Right, v, d - 1)
    }
}

func addOneRow(root *TreeNode, v int, d int) *TreeNode {
    if d == 1 {
        return &TreeNode{Val: v, Left: root}
    }

    solve(root, v, d)
    return root
}
