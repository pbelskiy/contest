class Solution:
    # 12 minutes for solution code

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        def get_diagonal(y, x, r):
            a = []

            while x >= 0 and y < n:
                a.append(mat[y][x])
                y += 1
                x -= 1

            if r % 2 == 0:
                return reversed(a)

            return a

        r = 0
        d = []

        for x in range(m):
            d.extend(get_diagonal(0, x, r))
            r += 1

        for y in range(1, n):
            d.extend(get_diagonal(y, m - 1, r))
            r += 1

        return d
