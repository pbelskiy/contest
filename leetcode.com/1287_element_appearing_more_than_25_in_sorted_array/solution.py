class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return collections.Counter(arr).most_common(1)[0][0]
