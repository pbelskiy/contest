class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return sorted(itertools.product(nums1, nums2), key=lambda t: t[0]+t[1])[:k]
