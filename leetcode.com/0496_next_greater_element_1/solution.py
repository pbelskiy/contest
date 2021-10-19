class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []

        for n1 in nums1:
            found = False
            for n2 in nums2:
                if found and n2 > n1:
                    arr.append(n2)
                    break
                if n2 == n1:
                    found = True
            else:
                arr.append(-1)

        return arr
