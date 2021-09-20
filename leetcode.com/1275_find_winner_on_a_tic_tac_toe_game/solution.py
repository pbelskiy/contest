class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' '] * 3 for _ in range(3)]

        player_a = True

        # fill
        for y, x in moves:
            if player_a:
                grid[y][x] = 'X'
            else:
                grid[y][x] = 'O'

            player_a = not player_a

        # check
        for y in range(3):
            if grid[y][0] == grid[y][1] == grid[y][2] and grid[y][2] != ' ':
                return 'A' if grid[y][0] == 'X' else 'B'

        for x in range(3):
            if grid[0][x] == grid[1][x] == grid[2][x] and grid[2][x] != ' ':
                return 'A' if grid[0][x] == 'X' else 'B'

        if grid[0][0] == grid[1][1] == grid[2][2] and grid[2][2] != ' ':
            return 'A' if grid[1][1] == 'X' else 'B'

        if grid[0][2] == grid[1][1] == grid[2][0] and  grid[2][0] != ' ':
            return 'A' if grid[1][1] == 'X' else 'B'

        if len(moves) != 9:
            return 'Pending'

        return 'Draw'
