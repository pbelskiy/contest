"""
To simplify solution, start to check is array sorted from end,
if i th number is unsorted try to decompose the number, return
number of steps needed and minimal number in decomposed list.

Example:
nums = [1,20,3]

Here we need to decompose 20 into list of numbers less or equal
to 3. So there are few variants such as:

20 = 6+6+6+2 (steps = 3, minumum = 2)
20 = 5+5+5+5 (steps = 3, minumum = 5)

Three steps of last variant:
        20
    10      10
 5     5  5     5

Our goal here is to maximize the minumum to get efficient result
on next steps.

TC: O(N)
SC: (1)
"""
class Solution:

    def solve(self, target, right):
        d, m = divmod(target, right)
        if m == 0:
            return d - 1, right

        return d, int(target / (d + 1))

    def minimumReplacement(self, nums: List[int]) -> int:
        t = 0

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                continue

            s, m = self.solve(nums[i], nums[i + 1])
            nums[i] = m
            t += s

        return t
