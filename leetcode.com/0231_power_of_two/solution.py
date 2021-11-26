class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 0 else bin(n).count('1') == 1

#         v = 1
#         for i in range(32):
#             if (1 << i) == n:
#                 return True
#         return False
