class Solution:
    def customSortString(self, order: str, string: str) -> str:
        h = {ch: i for i, ch in enumerate(order)}
        s = list(string)
        s.sort(key=lambda v: h.get(v, ord(v) + 27))
        return ''.join(s)
