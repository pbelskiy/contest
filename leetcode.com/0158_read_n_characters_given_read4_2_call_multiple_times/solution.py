class Solution:

    def __init__(self):
        a = []
        while True:
            b = [' ', ' ', ' ', ' ']
            r = read4(b)
            a.extend(b[:r])
            if r == 0:
                break

        self.a = a
        self.i = 0

    def read(self, buf: List[str], n: int) -> int:
        r = 0

        for j in range(min(n, len(self.a) - self.i)):
            buf[j] = self.a[self.i]
            self.i += 1
            r += 1

        return r
