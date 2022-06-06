class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def is_conflict(p, cy, cx):
            for y, x in p:
                if y == cy or x == cx:
                    return True
                if abs(cy - y) == abs(cx - x):
                    return True

            return False

        def dfs(r, p, s):

            if r == 0:
                m = [['.']*n for _ in range(n)]
                for y, x in p:
                    m[y][x] = 'Q'
                res.append([''.join(r) for r in m])
                return

            for y in range(s, n):
                for x in range(n):
                    if is_conflict(p, y, x):
                        continue

                    p.append((y, x))
                    dfs(r - 1, p, y + 1)
                    p.pop()

        res = []
        dfs(n, [], 0)
        return res
