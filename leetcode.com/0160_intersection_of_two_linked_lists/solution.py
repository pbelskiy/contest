class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        while headA:
            visited.add(headA)
            headA = headA.next

        while headB:
            if headB in visited:
                return headB
            headB = headB.next

        return None
