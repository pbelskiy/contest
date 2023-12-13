class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        mr = list(zip(*mat))
        t = 0
        h, w = len(mat), len(mat[0])

        for y in range(h):
            for x in range(w):
                if mat[y][x] == 0:
                    continue

                if sum(mat[y]) > 1:
                    continue

                if sum(mr[x]) > 1:
                    continue

                t += 1

        return t
