class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1

        left = 0
        right = 1

        even = arr[0] < arr[1]
        size = 1

        while right < len(arr):
            if (even is False and arr[right - 1] <= arr[right]) or \
               (even is True and arr[right - 1] >= arr[right]):
                left = right - 1
                right += 1

                if arr[left] == arr[left + 1]:
                    left += 1

                continue

            right += 1
            size = max(size, right - left)
            even = bool(not even)

        return size
