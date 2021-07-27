class Solution:
    def calc(self, n: int, depth: int) -> int:
        v = n
        op = -1

        for d in range(n - 1, 0, -1):
            op += 1
            if op == 0:
                v = v * d

            elif op == 1:
                v = v // d

            elif op == 2:
                if depth == 0:
                    v = v + d
                else:
                    v = v - d

            else:
                if depth > 0:
                    v = v + self.calc(d, depth + 1)
                else:
                    v = v - self.calc(d, depth + 1)
                break

        return v

    def clumsy(self, n: int) -> int:
        return self.calc(n, 0)
