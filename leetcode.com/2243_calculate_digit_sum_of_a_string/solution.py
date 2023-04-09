class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            ns = ''
            for i in range(math.ceil(len(s) / k)):
                chunk = s[i*k:i*k+k]
                ns += str(sum(map(int, chunk)))
            s = ns

        return s
