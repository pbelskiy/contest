class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1

        while True:
            for k, v in Counter(str(n)).items():
                if int(k) != int(v):
                    n += 1
                    break
            else:
                return n
