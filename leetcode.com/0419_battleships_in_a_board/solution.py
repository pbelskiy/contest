class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        def erase(y, x):
            q = collections.deque([(y, x)])

            while q:
                y, x = q.popleft()

                for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                    if not (0 <= dy < h and 0 <= dx < w):
                        continue
                    if board[dy][dx] == 'X':
                        board[dy][dx] = '.'
                        q.append((dy, dx))

        total = 0
        h, w = len(board), len(board[0])

        for y in range(h):
            for x in range(w):
                if board[y][x] == 'X':
                    erase(y, x)
                    total += 1

        return total
