class UndergroundSystem:

    def __init__(self):
        self.users = dict()
        self.total = collections.defaultdict(lambda: collections.defaultdict(int))
        self.count = collections.defaultdict(lambda: collections.defaultdict(int))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.users.pop(id)
        self.total[startStation][stationName] += t - startTime
        self.count[startStation][stationName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total[startStation][endStation] / self.count[startStation][endStation]
