class Solution:
    def findLucky(self, arr: List[int]) -> int:
        value = -1

        for k, v in collections.Counter(arr).items():
            if k == v:
                value = max(value, k)

        return value
