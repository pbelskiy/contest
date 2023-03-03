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

    # TLE (13/19)
    def qsort(self, a, l, r):
        if l < r:
            q = self.partition(a, l, r)
            self.qsort(a, l, q)
            self.qsort(a, q + 1, r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.qsort(nums, 0, len(nums) - 1)
        return nums



class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # 1800 ms (19/19 TCs)
        def mergesort(a):
            if len(a) <= 1:
                return a

            mid = len(a) // 2
            left = mergesort(a[:mid])
            right = mergesort(a[mid:])

            new = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1

            new += left[i:]
            new += right[j:]
            return new

        # 1500 ms (19/19 TCs)
        def quicksort(a):
            if len(a) <= 1:
                return a

            p = random.choice(a)
            l = [n for n in a if n < p]
            e = [n for n in a if n == p]
            r = [n for n in a if n > p]

            return quicksort(l) + e + quicksort(r)

        return quicksort(nums)
