"""
Use hashmap to improve brute force performance.

TC: O(N)
SC: O(N+M)
"""
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.count1 = Counter(nums1)
        self.count2 = Counter(nums2)
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        x = self.nums2[index]
        self.nums2[index] += val
        self.count2[x] -= 1
        self.count2[x + val] += 1

    def count(self, tot: int) -> int:
        r = 0
        for k1, v1 in self.count1.items():
            x = tot - k1
            r += self.count2[x]*v1

        return r
