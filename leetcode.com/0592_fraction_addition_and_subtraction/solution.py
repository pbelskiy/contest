class Solution:
    def fractionAddition(self, s: str) -> str:
        p = []
        n = []

        # parse fractions
        E = r'\d+/\d+'
        for sign, fraction in zip(re.split(E, s), re.findall(E, s)):
            a, b = map(int, fraction.split('/'))
            n.append(b)
            p.append([a, b, sign])

        # get total sum
        d = math.lcm(*n)
        if s[0] == '-':
            p[0][0] = -p[0][0]

        for i in range(len(p)):
            p[i][0] *= d // p[i][1]

        t = p[0][0]
        for i in range(len(p) - 1):
            if p[i + 1][2] == '+':
                t += p[i + 1][0]
            else:
                t -= p[i + 1][0]

        # simplify final fraction
        for x in (2, 3, 5, 7):
            while t % x == 0 and d % x == 0:
                t, d = t // x, d // x

        # return result
        if t == 0:
            return '0/1'

        if d == 1:
            return f'{t}/1'

        p = '-' if t < 0 else ''
        t = abs(t)

        if t > d:
            return f'{p}{t}/{d}'

        return f'{p}{t}/{d}'
