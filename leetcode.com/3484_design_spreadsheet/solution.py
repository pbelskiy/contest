class Spreadsheet:

    def __init__(self, rows: int):
        self.d = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.d[cell] = value

    def resetCell(self, cell: str) -> None:
        self.d[cell] = 0

    def getValue(self, formula: str) -> int:
        a, b = formula[1:].split('+')
        
        a = int(a) if a.isdigit() else self.d[a]
        b = int(b) if b.isdigit() else self.d[b]

        return a + b

