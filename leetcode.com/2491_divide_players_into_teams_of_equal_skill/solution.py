"""
Calcualte target sum of each group, then sort and check is
it possible.

TC: O(sort)
SC: O(sort)
"""
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill) // 2
        s = sum(skill)

        if s % n != 0:
            return -1

        target = s // n
        skill.sort()

        chemistry = 0
        left, right = 0, len(skill) - 1

        while left <= right:
            if skill[left] + skill[right] != target:
                return -1

            chemistry += skill[left] * skill[right]

            left += 1
            right -= 1

        return chemistry
