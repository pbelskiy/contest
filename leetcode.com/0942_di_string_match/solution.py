class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        a = 0
        b = len(s)

        res = []

        for ch in s:
            if ch == 'I':
                res.append(a)
                a += 1
            else:
                res.append(b)
                b -= 1

        res.append(a)
        return res
