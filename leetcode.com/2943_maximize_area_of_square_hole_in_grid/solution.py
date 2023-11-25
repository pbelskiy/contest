class Solution:
    def maximizeSquareHoleArea(self, v: int, h: int, hBars: List[int], vBars: List[int]) -> int:

        def get_max_continuous(a):
            w, mh = 1, 1
            for i in range(len(a) - 1):
                if a[i] + 1 == a[i + 1]:
                    w += 1
                else:
                    mh = max(mh, w)
                    w = 1
            return max(mh, w)

        hBars.sort()
        vBars.sort()

        mh = get_max_continuous(hBars)
        mv = get_max_continuous(vBars)

        return min(mh + 1, mv + 1)**2
