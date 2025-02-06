class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = Counter()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    freq[nums[i]*nums[j]] += 1

        t = 0
        for k, v in freq.items():
            for _ in range(v - 2):
                t += v

        return t
