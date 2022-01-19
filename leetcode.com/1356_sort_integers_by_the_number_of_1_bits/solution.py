class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr.sort(key=lambda n: bin(n).count('1'))
        return arr
