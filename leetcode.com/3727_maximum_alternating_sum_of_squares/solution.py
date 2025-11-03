"""
Sort and use two pointers.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted([n**2 for n in nums])
        t = 0

        left = 0
        right = len(a) - 1

        while True:
            if right >= left:
                t += a[right]
                right -= 1
            else:
                break

            if left <= right:
                t -= a[left]
                left += 1
            else:
                break

        return t

