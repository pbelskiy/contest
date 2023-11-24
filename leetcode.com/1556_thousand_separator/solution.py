class Solution:
    def thousandSeparator(self, n: int) -> str:
        a = []
        for i, d in enumerate(reversed(str(n))):
            a.append(d)
            if (len(a) - a.count('.')) % 3 == 0 and i != len(str(n)) - 1:
                a.append('.')
        return ''.join(reversed(a))
