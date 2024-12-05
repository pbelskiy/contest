class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.count('L') != target.count('L'):
            return False

        if start.count('R') != target.count('R'):
            return False

        i = len(target) - 1
        j = len(start) - 1

        while i >= 0 and j >= 0:

            while i > 0 and target[i] == '_':
                i -= 1

            while j > 0 and start[j] == '_':
                j -= 1

            if start[j] != target[i]:
                return False

            if start[j] == 'R' and j > i:
                return False

            if start[j] == 'L' and j < i:
                return False

            i -= 1
            j -= 1

        return True
