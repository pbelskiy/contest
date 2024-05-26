class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        p = []

        for i in range(len(nums)):
            if nums[i] == x:
                p.append(i)

        r = []
        for q in queries:
            if q > len(p):
                r.append(-1)
            else:
                r.append(p[q - 1])

        return r
