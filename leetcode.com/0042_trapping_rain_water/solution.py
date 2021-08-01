#!/usr/bin/env python3

from typing import List


class Solution:

    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, 0

        if len(height) < 2:
            return total

        # find first non null
        while height[left] == 0 and left + 1 < len(height):
            left += 1
            right += 1

        while True:
            right += 1

            # find right edge of interval
            while True:
                right_orig = right

                try:
                    while height[left] > height[right] and right + 1 < len(height):
                        right += 1
                except IndexError:
                    return total

                if height[left] <= height[right]:
                    break

                height[left] -= 1
                right = right_orig

            minimum = min(height[left], height[right])
            while left < right:
                total += minimum - min(minimum, height[left])
                left += 1


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
print(Solution().trap([4,2,0,3,2,5]), 9)
print(Solution().trap([]), 0)
print(Solution().trap([1]), 0)
print(Solution().trap([0, 0]), 0)
print(Solution().trap([1, 1]), 0)
print(Solution().trap([1, 2, 1]), 0)
print(Solution().trap([1, 0, 1]), 1)
print(Solution().trap([2,0,1]), 1)
print(Solution().trap([4,9,8,4,0,3]), 3)
print(Solution().trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]), 26)
