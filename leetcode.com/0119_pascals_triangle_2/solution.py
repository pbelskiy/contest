class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        curr = prev = [1]

        for _ in range(rowIndex):
            curr = []
            for i in range(len(prev) + 1):
                if i == 0 or i == len(prev):
                    curr.append(1)
                else:
                    curr.append(prev[i - 1] + prev[i])

            prev = curr

        return curr
