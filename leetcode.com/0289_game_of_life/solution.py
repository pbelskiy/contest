class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        nb = copy.deepcopy(board)
        h, w = len(board), len(board[0])

        def get_neighbors(y, x):
            dirs = (
                (y + 1, x),
                (y - 1, x),
                (y, x + 1),
                (y, x - 1),
                (y - 1, x - 1),
                (y - 1, x + 1),
                (y + 1, x - 1),
                (y + 1, x + 1),
            )

            live = 0
            for dy, dx in dirs:
                if not (0 <= dy < h and 0 <= dx < w):
                    continue

                if board[dy][dx] == 1:
                    live += 1

            return live

        for y in range(h):
            for x in range(w):
                live = get_neighbors(y, x)

                if board[y][x] == 1:
                    if live < 2:
                        nb[y][x] = 0
                    elif live > 3:
                        nb[y][x] = 0
                elif live == 3:
                    nb[y][x] = 1

        board[:] = nb
