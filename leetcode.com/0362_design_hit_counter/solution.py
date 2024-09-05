class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        t = 0

        for i in range(bisect.bisect(self.hits, timestamp) - 1, -1, -1):
            if timestamp - self.hits[i] >= 300:
                break

            t += 1

        return t
