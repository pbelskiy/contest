"""
To improve N^2 brute force solution, we can see in example
that we need to know how XOR works and count of bits for
each position.

Example:
  nums1 = [1,2], nums2 = [3,4]

Binary representation:
1 001
2 010
-----
3 011
4 100

Bitwise calculation of all pairs:
0bit => (1^1) ^ (1^0) ^ (0^1) ^ (0^0) => 0 ^ 1 ^ 1 ^ 0 => 0
1bit => (0^1) ^ (0^0) ^ (1^1) ^ (1^0) => 1 ^ 0 ^ 0 ^ 1 => 0
2bit => (0^0) ^ (0^1) ^ (0^0) ^ (0^1) => 0 ^ 1 ^ 0 ^ 1 => 0

It doesn't matter XOR priority:
(1^1) ^ (1^0) ^ (0^1) ^ (0^0) => 1^1^1^0^0^1^0^0 => 0

So, we need to know count of bits for each position and
it means:
1) 0^0^0^0... (any count of zero is zero)
2) 1^1^0^1... (odd number of ones leads to 1)

TC: O(N)
SC: O(N)
"""
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = defaultdict(lambda: defaultdict(int))
        count2 = defaultdict(lambda: defaultdict(int))

        width = max(nums1 + nums2).bit_length()

        # get count of bits
        for i in range(width):
            for n in nums1:
                if n & (1 << i):
                    count1[i][1] += 1
                else:
                    count1[i][0] += 1

            for n in nums2:
                if n & (1 << i):
                    count2[i][1] += 1
                else:
                    count2[i][0] += 1

        # construct result
        result = 0

        for i in range(width):
            bits_count = 0

            bits_count += count1[i][0] * count2[i][1]
            bits_count += count1[i][1] * count2[i][1]
            bits_count += count1[i][1] * len(nums2)

            if bits_count % 2 == 1:
                result |= (1 << i)

        return result
