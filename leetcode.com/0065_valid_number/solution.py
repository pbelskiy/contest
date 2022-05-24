class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return s not in ('inf', '-inf', '+inf', 'Infinity', '-Infinity', '+Infinity')
        except ValueError:
            return False
