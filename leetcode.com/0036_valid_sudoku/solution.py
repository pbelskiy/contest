from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    continue

                target = board[x][y]

                # check horizontal-vertical
                for d in range(9):
                    if d != y and board[x][d] == target:
                        return False
                    if d != x and board[d][y] == target:
                        return False

                # check box
                for sx in range((x // 3)*3, (x // 3)*3 + 3):
                    for sy in range((y // 3)*3, (y // 3)*3 + 3):
                        if sx != x and sy != y and board[sx][sy] == target:
                            return False

        return True


case = [
    ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
    ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
    ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
    ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
    ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
    ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
    ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
    ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
    ['.', '.', '.', '.', '8', '.', '.', '7', '9']
]

Solution().isValidSudoku(case)
