class NumberContainers:

    def __init__(self):
        self.i = {}
        self.n = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.i:
            n = self.i[index]
            if n == number:
                return
            self.n[n].remove(index)

        self.i[index] = number
        bisect.insort(self.n[number], index)

    def find(self, number: int) -> int:
        if not self.n[number]:
            return -1
        return self.n[number][0]
