class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        def fill(l, r, ch):
            for i in range(l, r + 1):
                arr[i] = ch

        arr = list(dominoes)
        l = 0
        r = None

        for i, ch in enumerate(arr):
            if ch == 'L' and r is None:
                fill(l, i, ch)
            elif ch == 'L' and r is not None:
                mid = (i - r - 1) // 2
                fill(r + 1, r + mid, 'R')
                fill(i - mid, i - 1, 'L')
                r = None
                l = i
            elif ch == 'R':
                if r is not None:
                    fill(r, i, 'R')
                r = i

        if r is not None:
            fill(r, len(arr) - 1, 'R')

        return ''.join(arr)
