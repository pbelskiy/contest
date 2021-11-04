class Solution:
    def originalDigits(self, s: str) -> str:
        l = []
        cnt = collections.Counter(s)

        table = (
            ('z', 'zero', '0', collections.Counter('zero')),
            ('w', 'two', '2', collections.Counter('two')),
            ('u', 'four', '4', collections.Counter('four')),
            ('x', 'six', '6', collections.Counter('six')),
            ('g', 'eight', '8', collections.Counter('eight')),
            ('o', 'one', '1', collections.Counter('one')),
            ('t', 'three', '3', collections.Counter('three')),
            ('f', 'five', '5', collections.Counter('five')),
            ('s', 'seven', '7', collections.Counter('seven')),
            ('n', 'nine', '9', collections.Counter('nine')),
        )

        for ch, d, v, c in table:
            while cnt[ch] > 0:
                cnt -= c
                l.append(v)

        return ''.join(sorted(l))
