class MyCalendarTwo:

    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:

        def is_overlaped(booked):
            for i in range(len(booked)):
                for j in range(len(booked)):
                    if i == j:
                        continue

                    if booked[i][0] < booked[j][1] and booked[j][0] < booked[i][1]:
                        return True

            return False

        booked = []
        for a, b in self.intervals:
            if a < end and start < b:
                booked.append([a, b])

        if len(booked) >= 2 and is_overlaped(booked):
            return False

        self.intervals.append((start, end))
        return True
