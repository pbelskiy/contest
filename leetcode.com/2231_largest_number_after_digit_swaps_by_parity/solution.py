class Solution:
    def largestInteger(self, num: int) -> int:
        odd, even = [], []

        for n in str(num):
            if int(n) % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        odd.sort()
        even.sort()

        s = ''
        for n in str(num):
            if int(n) % 2 == 0:
                s += even.pop()
            else:
                s += odd.pop()

        return int(s)
