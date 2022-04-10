class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[''] * (len(s)) for _ in range(numRows)]

        d, y, x = True, 0, 0

        for ch in s:
            rows[y][x] = ch

            if d:
                if y + 1 < numRows:
                    y += 1
                else:
                    d = not d
                    y -= 1
                    x += 1
            else:
                if y > 0:
                    y -= 1
                    x += 1
                else:
                    d = not d
                    y += 1

        res = ''
        for r in rows:
            res += ''.join(r)

        return res
