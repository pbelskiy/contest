/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func solve(node *TreeNode, prev **TreeNode, key int) {
    if node == nil {
        return   
    }
    
    if key < node.Val {
        solve(node.Left, &node.Left, key)
        return
    }

    if key > node.Val {
        solve(node.Right, &node.Right, key)
        return
    }
    
    if node.Left == nil && node.Right == nil {
        *prev = nil
        return
    }
    
    if node.Left != nil && node.Right != nil {
        var st *TreeNode = node.Right
        
        for st != nil {
            if st.Left == nil {
                solve(node, &node.Right, st.Val)
                node.Val = st.Val
                return
            }
            
            st = st.Left
        } 
        
        return
    }

    if node.Left == nil {
        *prev = node.Right
    } else {
        *prev = node.Left
    }
}

func deleteNode(root *TreeNode, key int) *TreeNode {
    solve(root, &root, key)
    return root
}
