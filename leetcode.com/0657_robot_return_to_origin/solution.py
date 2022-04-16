class Solution:
    def judgeCircle(self, moves: str) -> bool:
        y = x = 0

        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y -= 1
            else:
                y += 1

        return y == x == 0

