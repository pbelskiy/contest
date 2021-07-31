#!/usr/bin/env python3

from typing import List


class Solution:

    def r2l(self, height, covered) -> int:
        left, right = len(height) - 1, len(height) - 1

        # find first non null
        while height[right] == 0 and right > 0:
            right -= 1

        left -= 1
        while height[right] > height[left] and left > 0:
            left -= 1

        # print('l2r', left, right)

        if (left, right) in covered:
            return 0

        minimum = min(height[left], height[right])
        # print('min =', minimum)
        total = 0
        left += 1
        while left < right:
            total += minimum - height[left]
            left += 1

        return total

    def trap(self, height: List[int]) -> int:
        total = 0
        left, right = 0, 0

        covered = []

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

                # print(left, right)
                try:
                    while height[left] > height[right] and right + 1 < len(height):
                        right += 1
                except IndexError:
                    return total + self.r2l(height, covered)

                if height[left] <= height[right]:
                    break

                left = right_orig
                right = right_orig + 1

            if right - left == 1:
                left = right
                continue

            # print('left =', left, 'right =', right, height[left:right + 1])

            minimum = min(height[left], height[right])

            covered.append((left, right))
            while left < right:
                # print(f'total ({total}) += {minimum} - {height[left]}')
                total += minimum - height[left]
                left += 1

        # print('total =', total)
        return total


print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]), 6)
print(Solution().trap([4,2,0,3,2,5]), 9)
print(Solution().trap([]), 0)
print(Solution().trap([1]), 0)
print(Solution().trap([0, 0]), 0)
print(Solution().trap([1, 1]), 0)
print(Solution().trap([1, 2, 1]), 0)
print(Solution().trap([1, 0, 1]), 1)

print(Solution().trap([4,9,8,4,0,3]), 3)

print(Solution().trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]), 26)
