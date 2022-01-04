class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def dfs(i, s):
            if i >= len(words):
                combinations.append(s)
                return

            for ch in words[i]:
                dfs(i + 1, s + ch)

        combinations = []
        words = []

        for ch in digits:
            words.append(d[ch])

        if words:
            dfs(0, '')

        return combinations
