class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        odd = [i for i in range(len(nums)) if nums[i] % 2 == 1]
        even = [i for i in range(len(nums)) if nums[i] % 2 == 0]

        if abs(len(odd) - len(even)) > 1:
            return -1

        should = list(range(0, len(nums), 2))
        start_even = sum(abs(a - b) for a, b in zip(even, should))

        should = list(range(1, len(nums), 2))
        start_odd = sum(abs(a - b) for a, b in zip(even, should))

        if len(even) > len(odd):
            return start_even

        if len(even) < len(odd):
            return start_odd

        return min(start_even, start_odd)

