class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        t = (-1, -1, -1, -1)

        for h1, h2, m1, m2 in itertools.permutations(arr, 4):
            if h1*10 + h2 > 23:
                continue

            if m1*10 + m2 > 59:
                continue

            if (h1*10 + h2)*60 + (m1*10 + m2) > (t[0]*10 + t[1])*60 + (t[2]*10 + t[3]):
                t = (h1, h2, m1, m2)

        if sum(t) == -4:
            return ''

        return f'{t[0]}{t[1]}:{t[2]}{t[3]}'
