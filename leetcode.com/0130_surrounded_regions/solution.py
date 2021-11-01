class Solution:
    def solve(self, board: List[List[str]]) -> None:
        CELL_BUSY = 'X'
        CELL_FREE = 'O'
        CELL_CAPT = 'F'

        def dfs(y, x):
            for cy, cx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if not (0 <= cy < h and 0 <= cx < w):
                    continue
                if board[cy][cx] == CELL_FREE:
                    board[cy][cx] = CELL_CAPT
                    dfs(cy, cx)

        h, w = len(board), len(board[0])

        for y in range(h):
            if board[y][0] == CELL_FREE:
                dfs(y, 0)
            if board[y][w - 1] == CELL_FREE:
                dfs(y, w - 1)

        for x in range(w):
            if board[0][x] == CELL_FREE:
                dfs(0, x)
            if board[h - 1][x] == CELL_FREE:
                dfs(h - 1, x)

        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if board[y][x] == CELL_FREE:
                    board[y][x] = CELL_BUSY

        for y in range(h):
            for x in range(w):
                if board[y][x] == CELL_CAPT:
                    board[y][x] = CELL_FREE

