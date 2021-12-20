class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        output = []

        d = min([abs(a - b) for a, b in zip(arr, arr[1:])])

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == d:
                output.append([arr[i], arr[i + 1]])

        return output
