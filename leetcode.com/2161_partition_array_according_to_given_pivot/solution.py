class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []

        for n in nums:
            if n > pivot:
                right.append(n)
            elif n == pivot:
                mid.append(n)
            else:
                left.append(n)

        return left + mid + right
