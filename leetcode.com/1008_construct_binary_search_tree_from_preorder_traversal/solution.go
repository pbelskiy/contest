/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func bstAppend(node *TreeNode, val int) {
    for node != nil {
        if val >= node.Val {
            if node.Right == nil {
                node.Right = &TreeNode{val, nil, nil}
                return
            } else {
                node = node.Right
            }
        } else {
            if node.Left == nil {
                node.Left = &TreeNode{val, nil, nil}
                return
            } else {
                node = node.Left
            }
        }
    }
}

func bstFromPreorder(preorder []int) *TreeNode {
    root := &TreeNode{preorder[0], nil, nil}

    for i := 1 ; i < len(preorder) ; i++ {
        bstAppend(root, preorder[i])
    }

    return root
}
