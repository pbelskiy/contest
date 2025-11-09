class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        h = defaultdict(list)
        for i in range(len(nums)):
            h[nums[i]].append(i)

        d = float('inf')
        for a in h.values():
            if len(a) < 3:
                continue
            
            for i in range(len(a) - 2):
                d = min(d, abs(a[i] - a[i + 1]) + 
                           abs(a[i + 1] - a[i + 2]) + 
                           abs(a[i + 2] - a[i]))

        return d if d != float('inf') else -1

