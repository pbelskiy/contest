class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)

        for i, v in nums1 + nums2:
            d[i] += v

        return sorted(d.items(), key=lambda t: t[0])
