class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        pos = [p for p in range(len(grid[0]))]

        def move(touched, col, v):
            for i in range(len(pos)):
                if i in touched:
                    continue
                if pos[i] != col:
                    continue

                if v == 0:
                    pos[i] = -1
                elif v == -1:
                    pos[i] -= 1
                else:
                    pos[i] += 1

                touched.append(i)

        for row in grid:
            touched = list()
            for i in range(len(row)):
                if i == 0 and row[i] == -1:
                    move(touched, i, 0)
                elif i == len(row) - 1 and row[i] == 1:
                    move(touched, i, 0)
                elif i + 1 < len(row) and row[i] == 1 and row[i+1] == -1:
                    move(touched, i, 0)
                elif i - 1 > 0 and row[i] == -1 and row[i-1] == 1:
                    move(touched, i, 0)
                else:
                    move(touched, i, row[i])

        return pos
