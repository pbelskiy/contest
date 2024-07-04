class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            changed = True
            while changed:
                changed = False
                for i in range(len(row) - 1, 0, -1):
                    if row[i] == '.' and row[i - 1] == '#':
                        row[i], row[i - 1] = '#', '.'
                        changed = True

        return list(zip(*reversed(box)))
