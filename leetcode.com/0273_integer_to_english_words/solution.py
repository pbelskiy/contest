d1 = [
    '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
]

d2 = [
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
    'Seventeen', 'Eighteen', 'Nineteen',
]

d3 = [
    'Twenty', 'Thirty', 'Forty', 'Fifty',  'Sixty', 'Seventy', 'Eighty', 'Ninety',
]


def get_1_999(n):
    a = str(n)

    if len(a) == 1:
        return d1[int(a[0])]

    if len(a) < 3:
        a = '0' + a
        s = ''
    else:
        s = d1[int(a[0])] + ' Hundred '

    if int(a[1:]) < 10:
        s += d1[int(a[2])]
    elif int(a[1:]) < 20:
        s += d2[int(a[2])]
    else:
        s += d3[int(a[1]) - 2] + ' ' + d1[int(a[2])]

    return s.strip()


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'

        a = str(num)
        g = []
        i = len(a)

        while i > 0:
            i1 = i - 3
            i2 = i

            if i1 < 0:
                i1 = 0

            g.append(a[i1:i2])
            i -= 3

        s = ''
        d4 = ['', 'Thousand', 'Million', 'Billion']

        for i, p in enumerate(reversed(g)):
            j = len(g) - i

            ns = get_1_999(int(p))
            if not ns:
                continue

            s += ns + ' ' + d4[j - 1] + ' '

        return s.strip()