class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        mh = max(horizontalCuts[0], h - horizontalCuts[-1])
        mv = max(verticalCuts[0], w - verticalCuts[-1])

        for a, b in zip(horizontalCuts, horizontalCuts[1:]):
            mh = max(mh, b - a)

        for a, b in zip(verticalCuts, verticalCuts[1:]):
            mv = max(mv, b - a)

        return (mh*mv) % (10**9 + 7)
