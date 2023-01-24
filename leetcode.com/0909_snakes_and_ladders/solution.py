class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def p2c(p):
            y, x = divmod(p - 1, n)

            if y % 2 == 0:
                y = n - y - 1
            else:
                y = n - y - 1
                x = n - x - 1

            return y, x

        q = deque([(1, 0)])
        v = set()

        while q:
            p, m = q.popleft()

            y, x = p2c(p)
            if board[y][x] != -1:
                p = board[y][x]

            if p == n**2:
                return m

            for np in range(p + 1, min(p + 6, n**2) + 1):
                if np not in v:
                    q.append((np, m + 1))
                    v.add(np)

        return -1
