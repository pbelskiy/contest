class MyHashSet:

    def __init__(self):
        self.table = [list() for _ in range(10)]

    def add(self, key: int) -> None:
        if key not in self.table[hash(key) % 10]:
            self.table[hash(key) % 10].append(key)

    def remove(self, key: int) -> None:
        try:
            self.table[hash(key) % 10].remove(key)
        except ValueError:
            ...

    def contains(self, key: int) -> bool:
        return key in self.table[hash(key) % 10]
