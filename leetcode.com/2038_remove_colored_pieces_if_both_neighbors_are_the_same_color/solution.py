class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)

        if n <= 2:
            return False

        ap = 0
        bp = 0

        while True:

            # Alice pick
            while True:
                if ap + 2 >= n:
                    return False
                elif colors[ap+0] == colors[ap+1] == colors[ap+2] == 'A':
                    ap += 1
                    break
                else:
                    ap += 1

            # Bob pick
            while True:
                if bp + 2 >= n:
                    return True
                elif colors[bp+0] == colors[bp+1] == colors[bp+2] == 'B':
                    bp += 1
                    break
                else:
                    bp += 1
