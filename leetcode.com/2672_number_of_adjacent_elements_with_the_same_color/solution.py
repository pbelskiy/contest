"""
Just check on every query that somethings changed, and update our total.

TC: O(N)
SC: O(N)
"""
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0]*n
        answer = []
        total = 0

        for i, color in queries:
            if nums[i] == color:
                answer.append(total)
                continue

            if i + 1 < n and nums[i] != nums[i + 1] == color:
                total += 1
            if i + 1 < n and nums[i] and nums[i] == nums[i + 1] != color:
                total -= 1

            if i - 1 >= 0 and nums[i] != nums[i - 1] == color:
                total += 1
            if i - 1 >= 0 and nums[i] and nums[i] == nums[i - 1] != color:
                total -= 1

            nums[i] = color
            answer.append(total)

        return answer
