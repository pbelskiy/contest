def get_number_of_islands(binaryMatrix):

    def dfs(y, x):
        for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
            if not (0 <= cy < h and 0 <= cx < w):
                continue

            if binaryMatrix[cy][cx] == 0:
                continue

            binaryMatrix[cy][cx] = 0
            dfs(cy, cx)

    h, w = len(binaryMatrix), len(binaryMatrix[0])
    total = 0

    for y in range(h):
        for x in range(w):
            if binaryMatrix[y][x] == 0:
                continue

            dfs(y, x)
            total += 1

    return total
