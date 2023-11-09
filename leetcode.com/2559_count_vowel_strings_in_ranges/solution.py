class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = []

        t = 0
        for w in words:
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                t += 1
            prefix.append(t)

        res = []
        for left, right in queries:
            if left > 0:
                res.append(prefix[right] - prefix[left - 1])
            else:
                res.append(prefix[right])

        return res
