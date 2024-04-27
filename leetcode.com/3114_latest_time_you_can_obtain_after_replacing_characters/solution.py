class Solution:
    def findLatestTime(self, s: str) -> str:
        a = list(s)

        if a[0] == '?' and a[1] == '?':
            a[0] = a[1] = '1'

        if a[0] == '?':
            a[0] = '1' if int(a[1]) < 2 else '0'

        if a[1] == '?':
            a[1] = '9' if a[0] == '0' else '1'

        if a[3] == '?':
            a[3] = '5'

        if a[4] == '?':
            a[4] = '9'

        return ''.join(a)
