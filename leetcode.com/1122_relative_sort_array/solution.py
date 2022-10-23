class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort(key=lambda n: arr2.index(n) if n in arr2 else 1000 + n)
        return arr1
