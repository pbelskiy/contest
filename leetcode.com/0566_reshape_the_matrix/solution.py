class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        l = [item for sublist in mat for item in mat]

        if r*c != len(l):
            return mat

        m = []
        values = iter(l)

        try:
            for _ in range(r):
                row = []
                for column in range(len(l) // r):
                    row.append(next(values))
                m.append(row)
        except StopIteration:
            ...

        return m
