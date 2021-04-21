class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0

        for i, n in enumerate(sorted(heights)):
            if heights[i] != n:
                count += 1

        return count


