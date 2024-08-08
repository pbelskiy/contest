class Solution:
    def spiralMatrixIII(self, h: int, w: int, y: int, x: int) -> List[List[int]]:
        d = 1
        r = []

        if 0 <= y < h and 0 <= x < w:
            r.append([y, x])

        while len(r) < h*w:

            for _ in range(d):  # right
                x += 1
                if 0 <= y < h and 0 <= x < w:
                    r.append([y, x])

            for _ in range(d):  # down
                y += 1
                if 0 <= y < h and 0 <= x < w:
                    r.append([y, x])

            d += 1  # increase radius

            for _ in range(d):  # left
                x -= 1
                if 0 <= y < h and 0 <= x < w:
                    r.append([y, x])

            for _ in range(d):  # up
                y -= 1
                if 0 <= y < h and 0 <= x < w:
                    r.append([y, x])

            d += 1  # increase radius

        return r
