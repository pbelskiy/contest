/**
* Definition for a binary tree node.
* type TreeNode struct {
*     Val int
*     Left *TreeNode
*     Right *TreeNode
* }
*/

var r_depth int
var r_val int

func dfs(node *TreeNode, depth int, left bool) {
	if node == nil {
		return
	}

	if left && depth > r_depth {
		r_val = node.Val
		r_depth = depth
	}

	dfs(node.Left, depth + 1, true)
	dfs(node.Right, depth + 1, node.Left == nil)
}

func findBottomLeftValue(root *TreeNode) int {
	r_val = root.Val
	r_depth = 0
	dfs(root, 0, true)
	return r_val;
}
