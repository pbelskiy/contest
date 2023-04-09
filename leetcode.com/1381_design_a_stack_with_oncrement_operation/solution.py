class CustomStack:

    def __init__(self, maxSize: int):
        self.limit = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.limit:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1

        return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val
