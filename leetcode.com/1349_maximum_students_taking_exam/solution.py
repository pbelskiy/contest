class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:

        def get_row(row, mask):
            cnt = 0

            for x in range(len(row)):
                if row[x] == '.':
                    cnt += 1
                    if mask & (1 << cnt - 1):
                        row[x] = '+'

            return row

        def is_possible(y, curr, prev):
            """
            Convert two bitmask to rows and check if it possible to have
            """
            m  = [
                get_row(seats[y - 1][:], prev) if y > 0 else [0]*w,
                get_row(seats[y][:], curr),
            ]

            for x in range(w):
                if m[1][x] != '+':
                    continue
                if x > 0 and (m[1][x - 1] == '+' or m[0][x - 1] == '+'):
                    return False
                if x + 1 < w and (m[1][x + 1] == '+' or m[0][x + 1] == '+'):
                    return False

            return True

        @cache
        def dp(y, prev):
            if y == h:
                return 0

            b = 0

            # all possible combinations of current row occupation
            for curr in range(2**seats[y].count('.')):
                if is_possible(y, curr, prev):
                    b = max(b, dp(y + 1, curr) + curr.bit_count())

            return b

        h, w = len(seats), len(seats[0])
        return dp(0, 0)
