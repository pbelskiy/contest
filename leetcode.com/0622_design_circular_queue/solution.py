class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = deque()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.q.popleft()
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[-1]

    def isEmpty(self) -> bool:
        return len(self.q) == 0

    def isFull(self) -> bool:
        return len(self.q) == self.k
