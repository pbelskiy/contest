class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d = []
        for h, w in dimensions:
            d.append((sqrt(h**2 + w**2), h*w))
        d.sort()
        return d[-1][1]
