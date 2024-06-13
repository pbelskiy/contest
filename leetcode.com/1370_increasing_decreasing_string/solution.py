class Solution:
    def sortString(self, s: str) -> str:
        r = ''
        count = Counter(s)

        while count:

            for k in sorted(count.keys()):
                r += k
                count[k] -= 1
                if count[k] == 0:
                    del count[k]

            for k in sorted(count.keys(), reverse=True):
                r += k
                count[k] -= 1
                if count[k] == 0:
                    del count[k]

        return r
