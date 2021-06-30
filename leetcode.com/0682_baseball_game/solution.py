class Solution:
    def calPoints(self, ops: List[str]) -> int:
        values = []

        for op in ops:
            if op == 'C':
                values.pop()
            elif op == 'D':
                values.append(values[-1]*2)
            elif op == '+':
                values.append(values[-1] + values[-2])
            else:
                values.append(int(op))

        return sum(values)
