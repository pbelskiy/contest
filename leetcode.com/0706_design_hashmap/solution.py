class MyHashMap:

    def __init__(self):
        self.m = [-1]*(10**6 + 1)

    def put(self, key: int, value: int) -> None:
        self.m[key] = value

    def get(self, key: int) -> int:
        return self.m[key]

    def remove(self, key: int) -> None:
        self.m[key] = -1
