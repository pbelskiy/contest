class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = []

        a, b = s.split(':')

        for x in range(ord(a[:1]), ord(b[:1]) + 1):
            for y in range(int(a[1:]), int(b[1:]) + 1):
                cells.append(chr(x) + str(y))

        return cells
