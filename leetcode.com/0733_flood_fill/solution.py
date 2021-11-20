class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def dfs(y, x):
            image[y][x] = newColor

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue
                if image[cy][cx] == t and image[cy][cx] != newColor:
                    dfs(cy, cx)

        t = image[sr][sc]

        if t == newColor:
            return image

        h, w = len(image), len(image[0])
        dfs(sr, sc)
        return image
