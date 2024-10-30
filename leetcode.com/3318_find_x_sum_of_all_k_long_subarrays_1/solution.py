class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        def solve(a):
            count = Counter(a)

            t = 0
            for k, v in sorted(count.items(), key=lambda t: (-t[1], -t[0]))[:x]:
                t += k*v

            return t

        res = []
        for i in range(len(nums) - k + 1):
            res.append(solve(nums[i:i+k]))

        return res
