class Solution:
    def isPathCrossing(self, path: str) -> bool:
        y, x, v = 0, 0, set()

        for d in path:
            v.add((y, x))

            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            else:
                x -= 1

            if (y, x) in v:
                return True

        return False
