class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        t = 0

        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                b1, e1 = intervals[i]
                b2, e2 = intervals[j]

                if b2 <= b1 <= e2 or b2 <= e1 <= e2 :
                    t += 1

                elif b1 <= b2 <= e1 or b1 <= e2 <= e1:
                    t += 1
 
        return t

