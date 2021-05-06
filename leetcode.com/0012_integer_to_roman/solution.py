class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }

        values = sorted(d.keys(), reverse=True)

        s = ''
        while num > 0:
            for v in values:
                if num >= v:
                    s += d[v]
                    num -= v
                    break

        return s
