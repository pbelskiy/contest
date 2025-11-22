class Solution:
    def minimumFlips(self, n: int) -> int:
        s1 = bin(n)[2:]
        s2 = s1[::-1]

        return sum(int(ch1 != ch2) for ch1, ch2 in zip(s1, s2))

