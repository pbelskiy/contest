#!/usr/bin/env python3

from copy import deepcopy
from typing import List


class Solution:

    def get_local_candidates(self, x, y, board) -> bool:
        local_cnd = set()

        # check horizontal-vertical
        for d in range(9):
            local_cnd.add(board[x][d])
            local_cnd.add(board[d][y])

        # check box
        for sx in range((x // 3)*3, (x // 3)*3 + 3):
            for sy in range((y // 3)*3, (y // 3)*3 + 3):
                local_cnd.add(board[sx][sy])

        return local_cnd

    def fill(self, board: List[List[str]]) -> None:
        values = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        candidates = dict()

        found = True

        while found:
            found = False
            for x in range(9):
                for y in range(9):
                    if board[x][y] != '.':
                        continue

                    local_cnd = sorted(values - self.get_local_candidates(x, y, board))

                    if len(local_cnd) == 1:
                        candidates.pop((x, y), None)
                        board[x][y] = local_cnd[0]
                        found = True
                    else:
                        candidates[(x, y)] = local_cnd

            if found:
                continue

            # check by second factor
            for (x, y) in candidates:
                if board[x][y] != '.':
                    continue

                for cnd in candidates[(x, y)]:
                    for sy in range(9):
                        if sy == y:
                            continue
                        if (x, sy) not in candidates:
                            continue
                        if cnd in candidates[(x, sy)]:
                            break
                    else:
                        if cnd not in self.get_local_candidates(x, y, board):
                            board[x][y] = cnd
                            found = True
                            break

                    for sx in range(9):
                        if sx == x:
                            continue
                        if (sx, y) not in candidates:
                            continue
                        if cnd in candidates[(sx, y)]:
                            break
                    else:
                        if cnd not in self.get_local_candidates(x, y, board):
                            board[x][y] = cnd
                            found = True
                            break

        unsolved = 0
        for x in range(9):
            for y in range(9):
                if board[x][y] == '.':
                    unsolved += 1

        return candidates, unsolved

    def solveSudoku(self, board: List[List[str]]) -> None:
        candidates, unsolved = self.fill(board)
        if unsolved == 0:
            return

        for (x, y), variants in candidates.items():
            for v in variants:
                board[x][y] = v

                new_board = deepcopy(board)
                _, unsolved = self.fill(new_board)
                if unsolved == 0:
                    self.fill(board)
                    return

                board[x][y] = '.'


case1 = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9']
]

case2 = [
    ['.','.','9','7','4','8','.','.','.'],  # 1, 3, 5, 6
    ['7','.','.','.','.','.','.','.','.'],
    ['.','2','.','1','.','9','.','.','.'],
    ['.','.','7','.','.','.','2','4','.'],
    ['.','6','4','.','1','.','5','9','.'],
    ['.','9','8','.','.','.','3','.','.'],
    ['.','.','.','8','.','3','.','2','.'],
    ['.','.','.','.','.','.','.','.','6'],
    ['.','.','.','2','7','5','9','.','.']
]

case5 = [
    ["1",".",".",".","7",".",".","3","."],
    ["8","3",".","6",".",".",".",".","."],
    [".",".","2","9",".",".","6",".","8"],
    ["6",".",".",".",".","4","9",".","7"],
    [".","9",".",".",".",".",".","5","."],
    ["3",".","7","5",".",".",".",".","4"],
    ["2",".","3",".",".","9","1",".","."],
    [".",".",".",".",".","2",".","4","3"],
    [".","4",".",".","8",".",".",".","9"]
]

Solution().solveSudoku(case5)

from pprint import pprint
pprint(case5)
