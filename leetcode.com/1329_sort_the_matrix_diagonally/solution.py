class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        def sort_diagonal(sy, sx):
            found = True
            while found:
                found = False
                y, x = sy, sx

                while True:
                    if not (0 <= y + 1 < h and 0 <= x + 1 < w):
                        break

                    if mat[y][x] > mat[y + 1][x + 1]:
                        mat[y][x], mat[y + 1][x + 1] = mat[y + 1][x + 1], mat[y][x]
                        found = True

                    y += 1
                    x += 1

        h, w = len(mat), len(mat[0])

        for y in range(h):
            sort_diagonal(y, 0)

        for x in range(w):
            sort_diagonal(0, x)

        return mat
