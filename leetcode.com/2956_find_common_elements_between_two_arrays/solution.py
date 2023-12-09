class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)

        t1, t2 = 0, 0
        for n in nums1:
            if n in s2:
                t1 += 1

        for n in nums2:
            if n in s1:
                t2 += 1

        return [t1, t2]
