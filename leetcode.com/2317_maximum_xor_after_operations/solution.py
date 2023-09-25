"""
First of all it's easy taks, if we look create table of binary
representation of nums, it will be clear that anser is OR sum.

For example [1,2,3,9,2]

1 - 0001
2 - 0010
3 - 0011
9 - 1001
2 - 0010

Using `nums[i] AND (nums[i] XOR x)` we actually can zero any i th bit.

So it's clear that if i th bit is 0 everywhere, we cannot convert it
to 1, if any i th bit is 1 anywhere, we can conver rest of it to zero.

So our result will be sum of OR.

TC: O(N)
SC: O(1)
"""
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        r = 0
        for n in nums:
            r |= n
        return r
