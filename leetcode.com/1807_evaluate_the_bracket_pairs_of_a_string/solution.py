class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k: v for k, v in knowledge}
        l = s.split('(')
        res = l[0]

        for e in l[1:]:
            k, v = e.split(')')
            res += d.get(k, '?') + v

        return res
