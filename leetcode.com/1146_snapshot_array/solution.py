class SnapshotArray:

    def __init__(self, length: int):
        self.curr = collections.defaultdict(int)
        self.list = []

    def set(self, index: int, val: int) -> None:
        self.curr[index] = val

    def snap(self) -> int:
        self.list.append(copy.deepcopy(self.curr))
        return len(self.list) - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.list[snap_id][index]
