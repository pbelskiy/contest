class MapSum:

    def __init__(self):
        self.h = {}

    def insert(self, key: str, val: int) -> None:
        self.h[key] = val

    def sum(self, prefix: str) -> int:
        return sum([self.h[k] for k in self.h if k.startswith(prefix)])
