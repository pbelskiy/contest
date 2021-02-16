/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

 func deleteDuplicates(head *ListNode) *ListNode {
    var target = -101
    var begin, curr, prev *ListNode

    begin = head
    curr = head
    prev = nil

    for curr != nil {

        /* find duplicated value */
        if (curr.Next != nil && curr.Val == curr.Next.Val) {
            target = curr.Val
        }

        if (curr.Val != target) {
            prev = curr
            curr = curr.Next
            continue
        }

        for curr != nil && curr.Val == target {

            if (curr == begin) {
                begin = curr.Next
                curr = begin
            } else {
                curr = curr.Next
                prev.Next = curr
            }
        }
    }

    return begin
}
