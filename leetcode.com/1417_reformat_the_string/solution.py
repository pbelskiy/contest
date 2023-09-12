class Solution:
    def reformat(self, s: str) -> str:
        a, b = [], []

        for ch in s:
            if ch.isdigit():
                a.append(ch)
            else:
                b.append(ch)

        if abs(len(a) - len(b)) > 1:
            return ''

        if len(a) < len(b):
            a, b = b, a

        result = []
        for a, b in zip_longest(a, b, fillvalue=''):
            result.extend([a, b])

        return ''.join(result)
