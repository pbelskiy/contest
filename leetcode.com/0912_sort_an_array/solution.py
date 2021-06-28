class Solution:

    def partition(self, a, l, r):
        v = a[(l + r) // 2]
        i = l
        j = r

        while i <= j:
            while a[i] < v:
                i += 1
            while a[j] > v:
                j -= 1

            if i >= j:
                break

            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

        return j

    def qsort(self, a, l, r):
        if l < r:
            q = self.partition(a, l, r)
            self.qsort(a, l, q)
            self.qsort(a, q + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsort(nums, 0, len(nums) - 1)
        return nums
