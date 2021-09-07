func reverseList(head *ListNode) *ListNode {
    if head == nil {
        return head
    }

    var values []int

    for head != nil {
        values = append(values, head.Val)
        head = head.Next
    }

    node := &ListNode{}
    head = node

    for i := len(values) - 1; i >= 0 ; i-- {
        node.Val = values[i]

        if i != 0 {
            node.Next = &ListNode{}
            node = node.Next
        }
    }

    return head
}
