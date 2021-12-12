class SORTracker:

    def __init__(self):
        self.d = collections.defaultdict(list)
        self.i = -1

    def add(self, name: str, score: int) -> None:
        self.d[score].append(name)
        self.d[score].sort()

    def get(self) -> str:
        self.i += 1
        j = self.i

        for k in sorted(self.d.keys(), reverse=True):
            if j >= len(self.d[k]):
                j -= len(self.d[k])
            else:
                return self.d[k][j]
