class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:

        def dfs(node):
            if node:
                dfs(node.getNext())
                node.printValue()

        dfs(head)
