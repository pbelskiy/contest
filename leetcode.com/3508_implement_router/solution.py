class Router:

    def __init__(self, memoryLimit: int):
        self.p = set()
        self.q = deque()
        self.m = memoryLimit
        self.d = defaultdict(list)
  
    def _remove(self, source: int, destination: int, timestamp: int):
        self.p.remove((source, destination, timestamp))
        b = self.d[destination]
        i = bisect.bisect_left(b, timestamp)
        b.pop(i)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        k = (source, destination, timestamp)
        if k in self.p:
            return False

        # memory exceed
        if len(self.q) == self.m:
            self._remove(*self.q.popleft())

        self.q.append(k)
        self.p.add(k)
        self.d[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []

        k = self.q.popleft()
        self._remove(*k)
        return list(k)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        b = self.d[destination]
        i = bisect.bisect_left(b, startTime)
        j = bisect.bisect(b, endTime)
        return j - i

