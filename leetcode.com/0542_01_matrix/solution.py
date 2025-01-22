class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])

        dis = [[-1]*w for _ in range(h)]

        # collect start points
        q = deque()
        for y in range(h):
            for x in range(w):
                if mat[y][x] == 0:
                    q.append((y, x, 0))
                    dis[y][x] = 0

        while q:
            y, x, d = q.popleft()

            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if dis[dy][dx] == 0:
                    continue

                if dis[dy][dx] == -1 or dis[dy][dx] > d + 1:
                    q.append((dy, dx, d + 1))
                    dis[dy][dx] = d + 1

        return dis

