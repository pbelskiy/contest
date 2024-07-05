"""
Actually it's not strictly O(1), but it beats 80% of TCs.
"""
class Node:

    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class DoublyLinkedList:

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def add_right(self, data) -> Node:
        if not self.last:
            self.first = self.last = Node(data)
            return self.last

        prev = self.last
        self.last = Node(data, left=self.last)
        prev.right = self.last
        return self.last

    def add_left(self, data) -> Node:
        if not self.first:
            self.first = self.last = Node(data)
            return self.first

        prev = self.first
        self.first = Node(data, right=self.first)
        prev.left = self.first
        return self.first

    def remove(self, node: Node) -> None:
        if node.left is node.right is None:
            self.first = self.last = None
            return

        if node.left is None:
            self.first = node.right
            node.right.left = None
            return

        if node.right is None:
            self.last = node.left
            node.left.right = None
            return

        left, right = node.left, node.right
        left.right = right
        right.left = left


class AllOne:

    def __init__(self) -> None:
        self.lookup = {}
        self.dll = DoublyLinkedList()

    def inc(self, key: str) -> None:
        if key not in self.lookup:
            node = self.dll.add_left(dict(count=1, key=key))
            self.lookup[key] = node
            return

        node = self.lookup[key]
        node.data['count'] += 1

        # compare to count of node to right
        while node.right:
            if node.data['count'] <= node.right.data['count']:
                break

            # swap nodes
            tmp = node.right.data
            node.right.data = node.data
            node.data = tmp

            self.lookup[node.right.data['key']] = node.right
            self.lookup[node.data['key']] = node
            node = node.right

    def dec(self, key: str) -> None:
        node = self.lookup[key]
        node.data['count'] -= 1

        if node.data['count'] == 0:
            self.dll.remove(node)
            del self.lookup[node.data['key']]
            return

        # compare to count of node to left
        while node.left:
            if node.data['count'] >= node.left.data['count']:
                break

            # swap nodes
            tmp = node.left.data
            node.left.data = node.data
            node.data = tmp

            self.lookup[node.left.data['key']] = node.left
            self.lookup[node.data['key']] = node
            node = node.left

    def getMaxKey(self) -> str:
        if not self.dll.last:
            return ''
        return self.dll.last.data['key']

    def getMinKey(self) -> str:
        if not self.dll.first:
            return ''
        return self.dll.first.data['key']
