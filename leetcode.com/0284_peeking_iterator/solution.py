class PeekingIterator:
    def __init__(self, iterator):
        self.a = iterator.v
        self.i = 0

    def peek(self):
        return self.a[self.i]

    def next(self):
        self.i += 1
        return self.a[self.i - 1]

    def hasNext(self):
        return self.i < len(self.a)
