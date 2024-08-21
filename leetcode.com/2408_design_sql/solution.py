class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.d = defaultdict(dict)
        self.i = Counter()

    def insertRow(self, name: str, row: List[str]) -> None:
        self.i[name] += 1
        self.d[name][self.i[name]] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.d[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.d[name][rowId][columnId - 1]
