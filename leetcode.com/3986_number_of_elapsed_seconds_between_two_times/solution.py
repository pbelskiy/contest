class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h1, m1, s1 = map(int, startTime.split(':'))
        h2, m2, s2 = map(int, endTime.split(':'))

        t1 = h1*60*60 + m1*60 + s1
        t2 = h2*60*60 + m2*60 + s2

        return t2 - t1

