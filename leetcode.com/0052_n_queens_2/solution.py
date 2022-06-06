class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:

        def is_conflict(p, cy, cx):
            for y, x in p:
                if y == cy or x == cx:
                    return True
                if abs(cy - y) == abs(cx - x):
                    return True

            return False

        def dfs(r, p, s):
            if r == 0:
                return 1

            total = 0

            for y in range(s, n):
                for x in range(n):
                    if is_conflict(p, y, x):
                        continue

                    p.append((y, x))
                    total += dfs(r - 1, p, y + 1)
                    p.pop()

            return total

        return dfs(n, [], 0)
