"""
1134. Armstrong Number (Easy)

Given an integer n, return true if and only if it is an Armstrong
number.

The k-digit number n is an Armstrong number if and only if the kth
power of each digit sums to n.

Example 1:
Input: n = 153
Output: true
Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
"""
class Solution:
    def isArmstrong(self, n: int) -> bool:
        s = 0
        p = len(str(n))

        for i in str(n):
            s += int(i)**p

        return s == n
