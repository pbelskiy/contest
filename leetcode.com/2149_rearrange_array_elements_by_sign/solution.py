class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for n in nums:
            if n > 0:
                arr1.append(n)
            else:
                arr2.append(n)

        arr3 = []
        for i in range(len(nums) // 2):
            arr3.append(arr1[i])
            arr3.append(arr2[i])

        return arr3
