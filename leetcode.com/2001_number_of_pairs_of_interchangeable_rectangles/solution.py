class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        total = 0
        count = Counter()

        for a, b in rectangles:
            count[a / b] += 1

        for a, b in rectangles:
            r = a / b
            total += count[r] - 1
            count[r] -= 1

        return total
