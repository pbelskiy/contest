from sortedcontainers import SortedList


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        cost = 0

        for n in instructions:
            i = nums.bisect_right(n - 1)
            j = nums.bisect_left(n + 1)

            # there is no such number in nums
            if i == j:
                lt = i
                gt = len(nums) - i
            else:
                lt = i
                gt = len(nums) - j

            nums.add(n)
            cost = (cost + min(lt, gt)) % (10**9 + 7)

        return cost
