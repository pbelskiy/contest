class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        dirs = {
            'L': (0, -1),
            'R': (0, +1),
            'U': (-1, 0),
            'D': (+1, 0),
        }

        def get_moves(ins):
            moves = 0
            y, x = startPos

            for ch in ins:
                dy, dx = dirs[ch]

                y += dy
                x += dx

                if not (0 <= y < n and 0 <= x < n):
                    break

                moves += 1

            return moves

        res = []
        for i in range(len(s)):
            res.append(get_moves(s[i:]))

        return res
