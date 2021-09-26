class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = collections.defaultdict(int)

        for i, n in enumerate(nums):
            if n in d and abs(d[n] - i) <= k:
                return True

            d[n] = i

        return False
