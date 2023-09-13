"""
Simple idea here is go from left to right, trying to convert target to zero array.

If 1 on i index found (or 0 when flipped) then we do +1 operation and flip our target.

TC: O(N)
SC: O(1)
"""
class Solution:
    def minFlips(self, target: str) -> int:
        total = 0
        flipped = False

        for i in range(len(target)):
            if not flipped and target[i] == '0' or flipped and target[i] == '1':
                continue

            flipped = not flipped
            total += 1

        return total
