class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        s = []
        a = list(currentState)

        for i in range(len(a) - 1):
            if a[i] == a[i + 1] == '+':
                s.append(a[:])
                s[-1][i] = s[-1][i + 1] = '-'
                s[-1] = ''.join(s[-1])

        return s
