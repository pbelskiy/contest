class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        v = [min(r) for r in rectangles]
        return Counter(v)[max(v)]
