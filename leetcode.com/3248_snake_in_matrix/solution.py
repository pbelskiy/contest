class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        grid = [[0]*n for _ in range(n)]

        for y in range(n):
            for x in range(n):
                grid[y][x] = (y * n) + x

        y, x = 0, 0

        for command in commands:
            if command == 'RIGHT':
                x += 1
            elif command == 'LEFT':
                x -= 1
            elif command == 'DOWN':
                y += 1
            else:
                y -= 1

        return grid[y][x]
