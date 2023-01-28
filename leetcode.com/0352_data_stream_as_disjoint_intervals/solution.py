class SummaryRanges:

    def __init__(self):
        self.numbers = []

    def addNum(self, value: int) -> None:
        bisect.insort(self.numbers, value)

    def getIntervals(self) -> List[List[int]]:
        if len(self.numbers) == 0:
            return []

        intervals = []
        last = [self.numbers[0]]
        for i in range(len(self.numbers) - 1):
            if (self.numbers[i + 1] - self.numbers[i]) > 1:
                last.append(self.numbers[i])
                intervals.append(last)
                last = [self.numbers[i + 1]]

        last.append(self.numbers[-1])
        intervals.append(last)
        return intervals
