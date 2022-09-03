class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:

        def calc(selected):
            total = 0

            for row in mat:
                add = True
                for i, v in enumerate(row):
                    if v == 1 and selected[i] == 0:
                        add = False

                if add:
                    total += 1

            return total

        def permutations(size, count):
            for positions in itertools.combinations(range(size), count):
                p = [0]*size

                for i in positions:
                    p[i] = 1

                yield p

        r = 0
        for p in permutations(len(mat[0]), cols):
            r = max(r, calc(p))

        return r
