class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'gfi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        @cache
        def dfs(i):
            if i == len(pressedKeys):
                return 1

            total = 0

            for j in range(len(d[pressedKeys[i]])):
                k = i + j + 1

                if k > len(pressedKeys) or pressedKeys[i] != pressedKeys[k - 1]:
                    break

                total += dfs(k)

            return total % (10**9 + 7)

        return dfs(0)
