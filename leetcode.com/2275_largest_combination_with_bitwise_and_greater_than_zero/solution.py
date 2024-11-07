"""
Bitwise AND means need to find longest subsequence
of numbers which shares some i th bit.

Example: [16,17,71,62,12,24,14]

16 0010000
17 0010001
71 1000111
62 0111110
12 0001100
24 0011000
14 0001110
-------------
   1244432

Counter({
    0: 2,
    1: 3,
    2: 4,
    3: 4,
    4: 4,
    5: 1,
    6: 1
})

So maximum here is 4.

TC: O(N)
SC: O(1)
"""
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        count = Counter()

        for i in range(max(candidates).bit_length()):
            for n in candidates:
                if n & (1 << i):
                    count[i] += 1

        return max(count.values())
