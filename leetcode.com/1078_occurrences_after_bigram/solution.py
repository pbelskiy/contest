class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        arr = text.split()

        for i in range(len(arr) - 2):
            if arr[i] == first and arr[i + 1] == second:
                res.append(arr[i + 2])

        return res
