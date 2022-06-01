class Bitset:

    def __init__(self, size: int):
        self.k = size

        self.a = 0
        self.b = 2**size - 1

        self.a1 = 0
        self.b1 = size

        self.x = (2**self.k - 1)

    def fix(self, idx: int) -> None:
        mask = 1 << (self.k - idx - 1)

        if not(self.a & mask):
            self.a1 += 1
            self.b1 -= 1

            self.a |= mask
            self.b &= ~mask

    def unfix(self, idx: int) -> None:
        mask = 1 << (self.k - idx - 1)

        if self.a & mask:
            self.a1 -= 1
            self.b1 += 1

            self.a &= ~mask
            self.b |= mask

    def flip(self) -> None:
        self.a, self.b = self.b, self.a
        self.a1, self.b1 = self.b1, self.a1

    def all(self) -> bool:
        return self.a == self.x

    def one(self) -> bool:
        return self.a > 0

    def count(self) -> int:
        return self.a1

    def toString(self) -> str:
        return bin(self.a)[2:].zfill(self.k)
