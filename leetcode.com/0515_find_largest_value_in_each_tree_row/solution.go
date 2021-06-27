/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 func max(a, b int) int {
    if (a > b) {
        return a
    }

    return b
}

func largestValues(root *TreeNode) []int {
    if root == nil {
        return []int{}
    }

    values := []int{}
    queue := []*TreeNode{root}

    for len(queue) > 0 {
        val := queue[0].Val
        next_queue := []*TreeNode{}

        for _, item := range queue {
            val = max(val, item.Val)

            if item.Left != nil {
                next_queue = append(next_queue, item.Left)
            }

            if item.Right != nil {
                next_queue = append(next_queue, item.Right)
            }
        }

        values = append(values, val)
        queue = next_queue
    }

    return values
}