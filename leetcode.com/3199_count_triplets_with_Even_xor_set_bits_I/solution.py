"""
3199. Count Triplets with Even XOR Set Bits I (Easy)

Given three integer arrays a, b, and c, return the number
of triplets (a[i], b[j], c[k]), such that the bitwise XOR
of the elements of each triplet has an even number of set
bits.

Example 1:
Input: a = [1], b = [2], c = [3]
Output: 1
Explanation:
The only triplet is (a[0], b[0], c[0]) and their XOR is:
1 XOR 2 XOR 3 = 002.
"""
class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        t = 0

        for i in range(len(a)):
            for j in range(len(b)):
                for k in range(len(c)):
                    if (a[i] ^ b[j] ^ c[k]).bit_count() % 2 == 0:
                        t += 1

        return t
