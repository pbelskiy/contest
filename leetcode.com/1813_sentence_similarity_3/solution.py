class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            lo, hi = sentence1.split(), sentence2.split()
        else:
            lo, hi = sentence2.split(), sentence1.split()

        if len(lo) == len(hi) and lo != hi:
            return False

        if set(lo) - set(hi):
            return False

        def is_possible(lo, hi):
            j = 0
            for i in range(len(hi)):
                if hi[i] == lo[j]:
                    hi[i] = '*'
                    j += 1

                if j >= len(lo):
                    break

            s = ''.join(hi).strip('*')
            return '*' not in s and j >= len(lo)

        return is_possible(lo, hi[::]) or is_possible(lo[::-1], hi[::-1])
