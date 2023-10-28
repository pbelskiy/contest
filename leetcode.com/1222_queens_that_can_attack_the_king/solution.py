class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        board = [[False]*64 for _ in range(64)]
        for x, y in queens:
            board[x][y] = True

        def bfs(dx, dy):
            q = deque([king])
            while q:
                x, y = q.popleft()
                if board[x][y]:
                    res.append((x, y))
                    return

                if 0 <= x + dx < 64 and 0 <= y + dy < 64:
                    q.append((x + dx, y + dy))

        res = []
        for dx, dy in product([-1, 0, 1], repeat=2):
            if dx == 0 and dy == 0:
                continue
            bfs(dx, dy)

        return res
