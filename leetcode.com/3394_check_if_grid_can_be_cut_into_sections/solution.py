"""
Look on problem like on intervals, how many of
them are not overlapped.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        def is_possible(intervals):
            intervals = sorted(set(intervals))

            total = 0
            left, right = intervals[0]
            for i in range(1, len(intervals)):
                a, b = intervals[i]

                # overlapped -> merge
                if left <= a < right:
                    right = max(right, b)
                    continue

                total += 1
                left, right = a, b

            return total >= 2

        if is_possible([(y1, y2) for _, y1, _, y2 in rectangles]):
            return True

        if is_possible([(x1, x2) for x1, _, x2, _ in rectangles]):
            return True

        return False
