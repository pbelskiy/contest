class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]

        for a, b in zip(arr, arr[1:]):
            if b - a != d:
                return False

        return True
