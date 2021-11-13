class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        deltas = [0] * len(temperatures)

        for i, v in enumerate(temperatures):
            # remove all while it's lower than current value
            while stack and temperatures[stack[-1]] < v:
                deltas[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return deltas
