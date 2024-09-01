class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        r = []
        m = 0

        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > m:
                r.append(i)

            m = max(m, heights[i])

        return reversed(r)
