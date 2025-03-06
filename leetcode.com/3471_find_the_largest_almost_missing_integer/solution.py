class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter()

        for i in range(len(nums) - k + 1):
            a = set(nums[i:i+k])
            freq.update(a)

        x = (sorted(freq.items(), key=lambda t: (t[1], -t[0])))
        if x and x[0][1] == 1:
            return x[0][0]

        return -1
