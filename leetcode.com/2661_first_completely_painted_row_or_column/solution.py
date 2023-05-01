class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        h, w = len(mat), len(mat[0])

        d = {}
        for y in range(h):
            for x in range(w):
                d[mat[y][x]] = (y, x)

        x_axis, y_axis = defaultdict(int), defaultdict(int)

        for i, n in enumerate(arr):
            y, x = d[n]

            y_axis[y] += 1
            x_axis[x] += 1

            if y_axis[y] == w or x_axis[x] == h:
                return i
