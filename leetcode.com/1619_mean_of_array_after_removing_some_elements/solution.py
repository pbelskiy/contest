class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = int(len(arr)*0.05)
        return sum(arr[n:-n]) / (len(arr) - n*2)
