class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        a = ['0']

        for _ in range(n):
            p = a[-1]
            pr = list(p)

            for i in range(len(pr)):
                if pr[i] == '0':
                    pr[i] = '1'
                else:
                    pr[i] = '0'

            s = p + '1' + ''.join(pr[::-1])
            a.append(s)

        # for s in a:
        #     print(s)

        return a[-1][k - 1]
