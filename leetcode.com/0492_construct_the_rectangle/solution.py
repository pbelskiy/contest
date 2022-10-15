class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l = w = int(sqrt(area))

        while True:
            s = l*w
            if s == area:
                break
            if s < area:
                l += 1
            else:
                w -= 1

        return [l, w]
