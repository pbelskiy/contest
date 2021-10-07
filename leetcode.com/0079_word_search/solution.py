class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(y, x, p):
            if cache[(y, x, p)] >= 4:
                return False

            if p == len(word):
                return True

            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue

                if board[cy][cx] == word[p]:
                    cache[(y, x, p)] += 1
                    board[y][x], prev = '', board[y][x]
                    if dfs(cy, cx, p + 1):
                        return True
                    board[y][x] = prev

            return False

        h, w = len(board), len(board[0])
        cache = collections.defaultdict(int)

        for y, x in itertools.product(range(h), range(w)):
            if board[y][x] == word[0]:
                if dfs(y, x, 1):
                    return True

        return False
