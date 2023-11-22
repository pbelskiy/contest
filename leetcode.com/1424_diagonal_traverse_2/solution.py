"""
Sum of x, y coordinates belong to same diagonal.

[(0, 0), (1, 0), (2, 0),
 (0, 1), (1, 1), (2, 1),
 (0, 2), (1, 2), (2, 2)]
"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        h = []
        for y in range(len(nums)):
            for x in range(len(nums[y])):
                heappush(h, (x + y, x, y))

        res = []
        while h:
            _, x, y = heappop(h)
            res.append(nums[y][x])

        return res
