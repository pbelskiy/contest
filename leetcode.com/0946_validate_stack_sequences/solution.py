class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0

        while True:

            while i < len(pushed) and pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1

            if i >= len(pushed):
                break

            if pushed[i] == popped[j]:
                stack.append(pushed[i])
                i += 1

            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return i == j == len(pushed)
