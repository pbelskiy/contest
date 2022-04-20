class ATM:

    def __init__(self):
        self.count = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount: List[int]) -> None:
        self.count = [a + b for a, b in zip(self.count, banknotesCount)]

    def withdraw(self, amount: int) -> List[int]:
        count = [0, 0, 0, 0, 0]
        trans = [20, 50, 100, 200, 500]

        for i in range(len(self.count) - 1, -1, -1):
            total = min(self.count[i], amount // trans[i])
            amount -= total * trans[i]
            count[i] += total

        if amount != 0:
            return [-1]

        self.deposit(list(map(lambda v: -v, count)))
        return count
