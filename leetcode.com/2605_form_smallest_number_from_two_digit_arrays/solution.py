class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = set(nums1), set(nums2)
        for n in range(100):
            s = set(map(int, str(n)))
            if s1 & s and s2 & s:
                return n
