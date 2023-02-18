class Solution:
    def minMaxDifference(self, num: int) -> int:
        _max = float('-inf')
        for n in range(10):
            _max = max(_max, int(str(num).replace(str(n), '9')))

        _min = float('+inf')
        for n in range(10):
            _min = min(_min, int(str(num).replace(str(n), '0')))

        return _max - _min
