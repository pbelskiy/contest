class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        m = float('inf')

        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                nums3 = nums1[:]
                nums3.pop(i)
                nums3.pop(j - 1)

                d = set()
                for a, b in zip(sorted(nums2), sorted(nums3)):
                    d.add(a - b)

                if len(d) == 1:
                    m = min(m, next(iter(d)))

        return m
