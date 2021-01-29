/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    root := new(ListNode)
    last := root
    carry := 0

    for l1 != nil || l2 != nil {
        sum := carry
        
        if (l1 != nil) {
            sum += l1.Val            
            l1 = l1.Next
        } 
        
        if (l2 != nil) {
            sum += l2.Val            
            l2 = l2.Next
        }
        
        last.Val = sum % 10
        carry = sum / 10
        
        if (l1 != nil || l2 != nil) {
            last.Next = new(ListNode)
            last = last.Next
        }
    }
    
    for carry > 0 {
        last.Next = new(ListNode)
        last = last.Next
        
        last.Val = carry % 10
        carry = carry / 10
    }
    
    return root
}


