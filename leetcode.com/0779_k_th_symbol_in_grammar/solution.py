"""
Funny AC brute force solution with constructing large bitmap 2**30)
about 128 MB, and then getting k th element. To speed up our solution
we receive and cache largest possible row and cache it.
"""
class Solution:

    @classmethod
    @cache
    def build(cls, size):
        v = 1

        for _ in range(size):
            t = v  # save to temporary variable
            m = (1 << v.bit_length()) - 1
            v <<= v.bit_length()  # left shift to size of v
            v += (t ^ m)  # append inversed bits of previous v

        return v

    def kthGrammar(self, n: int, k: int) -> int:
        v = self.build(30)
        r = v >> (v.bit_length() - k)  # bitwise shift
        if r & 1:  # check k th element
            return 0
        return 1
