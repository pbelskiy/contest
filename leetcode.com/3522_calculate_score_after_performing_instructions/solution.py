class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        i = 0
        v = set()

        while 0 <= i < len(instructions):
            if i in v:
                break
            v.add(i)

            if instructions[i] == 'add':
                score += values[i]
                i += 1
                continue

            i += values[i]

        return score

