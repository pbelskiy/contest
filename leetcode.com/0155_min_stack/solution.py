class MinStack:

    def __init__(self):
        self.minimum = +2**31
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append((val, self.minimum))
        self.minimum = min(self.minimum, val)

    def pop(self) -> None:
        v, m = self.stack.pop()
        self.minimum = m

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minimum
