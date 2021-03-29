class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0]*n for _ in range(n)]

        v = 1
        x = -1
        y = 0

        while v <= n**2:

            # right
            x += 1
            while x < n:
                if m[y][x] != 0:
                    break
                m[y][x] = v
                v += 1
                x += 1

            # down
            y += 1
            while y < n:
                if m[y][x-1] != 0:
                    break
                m[y][x-1] = v
                v += 1
                y += 1

            # left
            x -= 1
            while x >= 0:
                if m[y-1][x-1] != 0:
                    break
                m[y-1][x-1] = v
                v += 1
                x -= 1

            # up
            y -= 1
            while y >= 0:
                if m[y-1][x] != 0:
                    break
                m[y-1][x] = v
                v += 1
                y -= 1

        return m
