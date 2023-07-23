class FrequencyTracker:

    def __init__(self):
        self.count = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        self.count[number] += 1

        self.freq[self.count[number] - 1] -= 1
        self.freq[self.count[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number not in self.count:
            return

        self.count[number] -= 1

        if self.count[number] == 0:
            del self.count[number]

        self.freq[self.count[number] + 1] -= 1
        self.freq[self.count[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0
