class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []

        for a in range(1, 1001):
            for b in range(1, 1001):
                r = customfunction.f(a, b)
                if r == z:
                    res.append([a, b])

                if r > z:
                    break

        return res
