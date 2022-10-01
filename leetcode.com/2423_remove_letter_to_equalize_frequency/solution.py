class Solution:
    def equalFrequency(self, word: str) -> bool:
        values = sorted(Counter(word).values())

        def test(v, i):
            v[i] -= 1
            if v[i] == 0:
                del v[i]

            return len(set(v)) == 1

        return test(values[:], 0) or test(values[:], len(values) - 1)
