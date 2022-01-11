class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIRS = ((0, 1), (-1, 0), (0, -1), (1, 0))

        x, y, d, p = 0, 0, DIRS[0], 0

        for _ in range(4):
            for cmd in instructions:

                if cmd == 'L':
                    p = p + 1 if p < 3 else 0
                    d = DIRS[p]
                    continue

                if cmd == 'R':
                    p = p - 1 if p > 0 else 3
                    d = DIRS[p]
                    continue

                y += d[0]
                x += d[1]

        return (x, y) == (0, 0)
