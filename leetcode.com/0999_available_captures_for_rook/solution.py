class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        rook_y, rook_x = None, None

        # find rook coordinates
        for y in range(8):
            for x in range(8):
                if board[y][x] == 'R':
                    rook_y = y
                    rook_x = x
                    break

        # left <-> right
        for start, finish, step in ((rook_x, -1, -1), (rook_x, 8, 1)):
            for x in range(start, finish, step):
                if board[rook_y][x] == 'B':
                    break
                if board[rook_y][x] == 'p':
                    count += 1
                    break

        # up <-> down
        for start, finish, step in ((rook_y, -1, -1), (rook_y, 8, 1)):
            for y in range(start, finish, step):
                if board[y][rook_x] == 'B':
                    break
                if board[y][rook_x] == 'p':
                    count += 1
                    break

        return count
