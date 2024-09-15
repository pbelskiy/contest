class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        res = []

        for n in nums:
            if n in seen:
                res.append(n)
            else:
                seen.add(n)

        return res
