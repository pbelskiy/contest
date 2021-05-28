class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        idx = s.find('6')
        if idx == -1:
            return num

        return int(s[:idx] + '9' + s[idx+1:])
