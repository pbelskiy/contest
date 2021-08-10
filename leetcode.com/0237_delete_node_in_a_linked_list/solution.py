class Solution:
    def deleteNode(self, node):
        last = None
        while node.next:
            node.val = node.next.val
            last = node
            node = node.next

        last.next = None
