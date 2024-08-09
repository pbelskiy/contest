"""
3032. Count Numbers With Unique Digits II (Easy)

Given two positive integers a and b, return the count of
numbers having unique digits in the range [a, b]  (inclusive).

Example 1:
    Input: a = 1, b = 20
    Output: 19
    Explanation: All the numbers in the range [1, 20] have unique
    digits except 11. Hence, the answer is 19.
"""
class Solution:
    def numberCount(self, a: int, b: int) -> int:
        t = 0

        for i in range(a, b + 1):
            if len(str(i)) == len(set(str(i))):
                t += 1

        return t
