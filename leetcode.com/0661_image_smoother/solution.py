class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        def get(y, x):
            points = (
                (y - 1, x - 1),
                (y - 1, x),
                (y - 1, x + 1),
                (y, x - 1),
                (y, x),
                (y, x + 1),
                (y + 1, x - 1),
                (y + 1, x),
                (y + 1, x + 1),
            )

            s, t = 0, 0
            for y, x in points:
                if not (0 <= y < h and 0 <= x < w):
                    continue

                s += img[y][x]
                t += 1

            return int(s / t)

        h, w = len(img), len(img[0])
        res = [[None]*w for _ in range(h)]

        for y in range(h):
            for x in range(w):
                res[y][x] = get(y, x)

        return res
