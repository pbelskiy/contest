func middleNode(head *ListNode) *ListNode {
    fast := head
    slow := head

    for fast != nil && fast.Next != nil {
        fast = fast.Next.Next
        slow = slow.Next
    }

    return slow
}
