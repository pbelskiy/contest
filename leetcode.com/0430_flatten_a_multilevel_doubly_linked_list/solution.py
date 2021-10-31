class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def dfs(node, last):
            if not node:
                return

            # skip linear links
            while node.next and node.child is None:
                node = node.next

            if node.child:
                node.child.prev = node
                ret = dfs(node.child, node.next)

                node.next = node.child
                node.child = None
                if ret:
                    node = ret

            if not node:
                return

            # skip linear links
            while node.next:
                node = node.next

            # next of last is last of prev level
            node.next = last
            if last:
                last.prev = node

            return last

        dfs(head, None)
        return head
