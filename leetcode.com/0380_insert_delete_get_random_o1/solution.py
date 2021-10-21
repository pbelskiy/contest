class RandomizedSet:

    def __init__(self):
        self.s = set()
        self.l = list()

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False

        self.s.add(val)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False

        self.s.remove(val)
        self.l.remove(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.l)
