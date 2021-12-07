class MyQueue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.insert(0, x)

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
