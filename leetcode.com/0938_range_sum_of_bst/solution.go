func rangeSumBST(root *TreeNode, low int, high int) int {
    if root == nil {
        return 0
    }

    sum := 0

    if low <= root.Val && root.Val <= high {
        sum += root.Val
    }

    return rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high) + sum
}
