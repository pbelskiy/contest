class Solution:
    def longestMountain(self, arr: List[int]) -> int:

        @cache
        def get_left(i):
            if i - 1 >= 0 and arr[i - 1] < arr[i]:
                return get_left(i - 1) + 1
            return 0

        @cache
        def get_right(i):
            if i + 1 < len(arr) and arr[i] > arr[i + 1]:
                return get_right(i + 1) + 1
            return 0

        m = 0
        for i in range(1, len(arr) - 1):
            if not (arr[i - 1] < arr[i] > arr[i + 1]):
                continue

            m = max(m, get_left(i) + get_right(i) + 1)

        return m
