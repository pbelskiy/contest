class Solution:
    def read(self, buf, n):
        i = 0

        while True:
            b = [' ', ' ', ' ', ' ']
            r = read4(b)

            for j in range(min(n, r)):
                buf[i] = b[j]
                i += 1
                n -= 1

            if r == 0 or n == 0:
                break

        return i
