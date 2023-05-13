class Solution:
    def countSeniors(self, details: List[str]) -> int:
        t = 0

        for d in details:
            if int(d[11:13]) > 60:
                t += 1

        return t
