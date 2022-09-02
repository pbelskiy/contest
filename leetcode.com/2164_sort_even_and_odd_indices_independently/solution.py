class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = sorted(nums[0::2])
        b = sorted(nums[1::2], reverse=True)

        r = []

        while a or b:
            if a:
                r.append(a.pop(0))
            if b:
                r.append(b.pop(0))

        return r
