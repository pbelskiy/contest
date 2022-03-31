class Solution:
    def minimumMoves(self, s: str) -> int:
        moves = 0
        a = list(s)

        while 'X' in a:
            for j in range(min(a.index('X') + 3, len(s))):
                a[j] = 'O'

            moves += 1

        return moves
