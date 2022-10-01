class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.v = [False]*n
        self.l = 0

    def upload(self, video: int) -> None:
        self.v[video - 1] = True

    def longest(self) -> int:
        if self.v[0] == False:
            return 0

        for i in range(self.l, self.n):
            if self.v[i] == False:
                self.l = i - 1
                break
        else:
            self.l = self.n - 1

        return self.l + 1
