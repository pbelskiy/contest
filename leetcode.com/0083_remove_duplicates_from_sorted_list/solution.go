/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteDuplicates(head *ListNode) *ListNode {
    curr := head

    for curr != nil {
        if curr.Next != nil && curr.Next.Val == curr.Val {
            curr.Next = curr.Next.Next
        } else {
            curr = curr.Next
        }
    }

    return head
}

