class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = int(''.join(map(str, b)))
        return pow(a, b, 1337)
