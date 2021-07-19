# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        nodes = []

        node = head
        while node:
            nodes.append(node)
            node = node.next

        head = None
        last = None

        for i in range(k - 1, len(nodes), k):
            if not head:
                head = nodes[i]

            for j in range(k - 1):
                if last:
                    last.next = nodes[i - j]

                nodes[i - j].next = nodes[i - j - 1]
                last = nodes[i - j - 1]

        d = len(nodes) % k
        if d == 0:
            last.next = None
        else:
            last.next = nodes[-d]

        return head
