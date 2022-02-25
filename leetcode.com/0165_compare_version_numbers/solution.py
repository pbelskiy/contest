class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')

        if len(nums1) > len(nums2):
            nums2.extend(['0'] * (len(nums1) - len(nums2)))
        elif len(nums2) > len(nums1):
            nums1.extend(['0'] * (len(nums2) - len(nums1)))

        for n1, n2 in zip(nums1, nums2):
            if int(n1) == int(n2):
                continue
            elif int(n1) > int(n2):
                return 1
            else:
                return -1

        return 0
