func pruneTree(root *TreeNode) *TreeNode {
    if root.Left != nil && pruneTree(root.Left) == nil {
        root.Left = nil
    }

    if root.Right != nil && pruneTree(root.Right) == nil {
        root.Right = nil
    }

    if root.Val == 0 && root.Left == nil && root.Right == nil {
        return nil
    }

    return root;
}
