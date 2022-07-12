class SmallestInfiniteSet:

    def __init__(self):
        self.values = list(range(1, 1001))

    def popSmallest(self) -> int:
        return self.values.pop(0)

    def addBack(self, num: int) -> None:
        if num in self.values:
            return

        bisect.insort(self.values, num)
