class Solution:
    def reformatNumber(self, number: str) -> str:
        s = number.replace(' ', '').replace('-', '')

        groups = []
        pos = 0

        while pos < len(s):
            if len(s) - pos == 4:
                groups.append(s[pos+0:pos+2])
                groups.append(s[pos+2:pos+4])
                pos += 4

            elif len(s) - pos >= 3:
                groups.append(s[pos:pos+3])
                pos += 3

            else:
                groups.append(s[pos:pos+2])
                pos += 2

        return '-'.join(groups)
