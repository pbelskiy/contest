class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not (0 < account1 <= self.n):
            return False

        if not (0 < account2 <= self.n):
            return False

        if self.balance[account1 - 1] < money:
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not (0 < account <= self.n):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not (0 < account <= self.n):
            return False

        if self.balance[account - 1] < money:
            return False

        self.balance[account - 1] -= money
        return True
