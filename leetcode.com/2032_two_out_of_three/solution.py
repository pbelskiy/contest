class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1 = set(nums1) & set(nums2)
        s2 = set(nums1) & set(nums3)
        s3 = set(nums2) & set(nums3)

        return s1 | s2 | s3
