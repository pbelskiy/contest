class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        def parse(s):
            days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            m, d = map(int, s.split('-'))
            return sum(days[:m - 1]) + d

        a1, a2 = parse(arriveAlice), parse(leaveAlice)
        b1, b2 = parse(arriveBob), parse(leaveBob)

        if a1 <= b1 <= b2 <= a2:
            return b2 - b1 + 1

        if b1 <= a1 <= a2 <= b2:
            return a2 - a1 + 1

        if a1 <= b1 <= a2:
            return a2 - b1 + 1

        if b1 <= a1 <= b2:
            return b2 - a1 + 1

        return 0
