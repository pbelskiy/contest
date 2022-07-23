class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = Counter()
        t = 0

        for n in nums:
            if n != 0:
                count[t] += 1
                t = 0
            else:
                t +=1

        count[t] += 1

        total = 0
        for k, v in count.items():
            total += (k*(k+1))/2*v

        return int(total)
