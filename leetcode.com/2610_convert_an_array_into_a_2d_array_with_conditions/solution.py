class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        matrix = []
        total = len(nums)

        while total > 0:
            row = []
            for k, v in count.items():
                if v == 0:
                    continue
                row.append(k)
                count[k] -= 1
                total -= 1

            matrix.append(row)

        return matrix
