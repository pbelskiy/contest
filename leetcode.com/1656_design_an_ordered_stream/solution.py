class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None]*n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        chunk = []

        i = self.ptr
        while i < len(self.stream) and self.stream[i]:
            chunk.append(self.stream[i])
            self.ptr += 1
            i += 1

        return chunk
