class MRUQueue:

    def __init__(self, n: int):
        self.q = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        n = self.q.pop(k - 1)
        self.q.append(n)
        return n
