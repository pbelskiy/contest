class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.a = []

    def insertFront(self, value: int) -> bool:
        if len(self.a) == self.k:
            return False

        self.a.append(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.a) == self.k:
            return False

        self.a.insert(0, value)
        return True

    def deleteFront(self) -> bool:
        if len(self.a) == 0:
            return False

        self.a.pop(-1)
        return True

    def deleteLast(self) -> bool:
        if len(self.a) == 0:
            return False

        self.a.pop(0)
        return True

    def getFront(self) -> int:
        if len(self.a) == 0:
            return -1

        return self.a[-1]

    def getRear(self) -> int:
        if len(self.a) == 0:
            return -1

        return self.a[0]

    def isEmpty(self) -> bool:
        return len(self.a) == 0

    def isFull(self) -> bool:
        return len(self.a) == self.k
