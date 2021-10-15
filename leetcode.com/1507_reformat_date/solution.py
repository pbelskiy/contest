class Solution:
    def reformatDate(self, date: str) -> str:
        M = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        d, m, y = date.split()

        d = int(d[:-2])
        m = M.index(m) + 1

        return f'{y}-{m:02d}-{d:02d}'
