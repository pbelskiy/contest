class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        a = []

        for y in range(cols):
            for x in range(rows):
                a.append((x, y))

        return sorted(a, key=lambda t: (abs(rCenter - t[0]) + abs(cCenter - t[1])))
