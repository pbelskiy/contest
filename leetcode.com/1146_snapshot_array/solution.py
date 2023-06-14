class SnapshotArray:
    MOD = 100

    def __init__(self, length: int):
        self.curr = defaultdict(int)
        self.list = []
        self.cache = {}

    def set(self, index: int, val: int) -> None:
        self.curr[index] = val

    def snap(self) -> int:
        self.list.append(self.curr)
        self.curr = defaultdict(int)
        snap_id = len(self.list) - 1

        return snap_id

    def get(self, index: int, snap_id: int) -> int:
        key = snap_id // self.MOD
        if key in self.cache:
            start = key * self.MOD
            d = self.cache[key].copy()
        else:
            start = 0
            d = defaultdict(int)

        for i in range(start, snap_id + 1):
            if i % self.MOD == 0 and i // self.MOD not in self.cache:
                self.cache[i // self.MOD] = d.copy()

            d |= self.list[i]

        return d[index]
