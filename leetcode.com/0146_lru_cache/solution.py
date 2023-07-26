class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, value) -> Node:
        node = Node(value)

        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

        return self.head

    def remove(self, node: Node) -> None:
        prv = node.prev
        nxt = node.next

        if prv:
            prv.next = nxt
        if nxt:
            nxt.prev = prv

        if node is self.head:
            self.head = nxt
        if node is self.tail:
            self.tail = prv


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.d = {}
        self.m = {}
        self.dll = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        self.dll.remove(self.m[key])
        self.m[key] = self.dll.append(key)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key] = value
            self.dll.remove(self.m[key])
            self.m[key] = self.dll.append(key)
            return

        if len(self.d) == self.capacity:
            node = self.dll.tail
            del self.d[node.data]
            del self.m[node.data]
            self.dll.remove(node)

        self.m[key] = self.dll.append(key)
        self.d[key] = value
